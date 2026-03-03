# evaluator.py
import math
import numpy as np

# Pesos (ajustables)
WEIGHTS = {
    "regulation": 0.35,
    "polaridad": 0.20,
    "tension_control": 0.20,
    "vulnerabilidad": 0.15,
    "response_rhythm": 0.10
}

def score_regulation(state_internal):
    # Regresión simple: "Calmado" > "Curioso" > "Dominante" > "Inseguro"
    mapping = {"Calmado": 1.0, "Curioso": 0.9, "Dominante": 0.8, "Inseguro": 0.4}
    return mapping.get(state_internal, 0.75)

def score_polarity(script_meta):
    # Más polaridad = mejor. Si el script contiene 'tension' y 'push-pull' asumimos bueno.
    txt = str(script_meta).lower()
    score = 0.6
    if "push" in txt or "push-pull" in txt or "tension" in txt:
        score = 1.0
    return score

def score_tension_control(script_meta):
    # si errores a evitar están presentes, asumimos moderado.
    return 0.85

def score_vulnerability(cierre_text):
    # Si el cierre contiene proyectos reales (IA, ritmos), mejor autenticidad
    s = cierre_text.lower()
    if "ritmo" in s or "ia" in s or "aeroespacial" in s or "arte" in s:
        return 1.0
    return 0.6

def score_response_rhythm(response_times):
    # response_times: list of latencias en segundos
    if not response_times:
        return 0.7
    avg = np.mean(response_times)
    # Ideal avg latency: 2.0 to 5.0 seconds -> calma y presencia
    if 2.0 <= avg <= 5.0:
        return 1.0
    # penaliza si muy rápido (<1.2s) o muy lento (>8s)
    if avg < 1.2:
        return 0.5
    if avg > 8.0:
        return 0.5
    # interpolate linearly
    return max(0.55, 1.0 - abs(3.5 - avg) / 6.0)

def presence_score(state_internal, script_meta, cierre_text, response_times):
    r = score_regulation(state_internal)
    p = score_polarity(script_meta)
    t = score_tension_control(script_meta)
    v = score_vulnerability(cierre_text)
    rr = score_response_rhythm(response_times)

    weighted = (r*WEIGHTS["regulation"] + p*WEIGHTS["polaridad"] +
                t*WEIGHTS["tension_control"] + v*WEIGHTS["vulnerabilidad"] +
                rr*WEIGHTS["response_rhythm"])
    # scale 0-100
    return round(weighted * 100, 1)