# generator.py
import random
from banks import APERTURAS, LECTURAS, TENSION, CIERRES
from banks import OBJETOS, CONTRASTES, EXTERNOS, INTERNOS, RIESGOS, PROYECTOS

def pick(seq):
    return random.choice(seq)

def generar_script(context, profile, state_internal, user_identity=None):
    # user_identity: texto corto sobre tus proyectos (para humanización)
    apertura = pick(APERTURAS).format(
        objeto=pick(OBJETOS),
        contraste=pick(CONTRASTES)
    )

    lectura = pick(LECTURAS).format(
        externo=pick(EXTERNOS),
        interno=pick(INTERNOS)
    )

    tension = pick(TENSION).format(
        riesgo=pick(RIESGOS)
    )

    cierre_template = pick(CIERRES)
    cierre = cierre_template.format(
        proyecto=user_identity or pick(PROYECTOS)
    )

    # metadata para evaluación y entrenamiento
    meta = {
        "context": context,
        "profile": profile,
        "state_internal": state_internal,
        "strategy": {
            "pieces": 4,
            "piece_templates": {
                "apertura": apertura,
                "lectura": lectura,
                "tension": tension,
                "cierre": cierre
            }
        },
        "activates": {
            "emotion": "curiosidad + leve desafío",
            "hormones": ["dopamina (anticipación)", "oxitocina (si hay conexión)"]
        },
        "errors_to_avoid": [
            "sonar necesitado",
            "acelerar el ritmo",
            "dar demasiados detalles para impresionar"
        ],
        "bodily_cues": "pecho abierto, respiración lenta, mandíbula relajada"
    }

    script_text = f"🔹 Apertura:\n{apertura}\n\n🔹 Lectura en frío:\n{lectura}\n\n🔹 Tensión (push-pull):\n{tension}\n\n🔹 Cierre / Humanización:\n{cierre}"

    return script_text, meta