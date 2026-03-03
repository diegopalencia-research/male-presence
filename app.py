# app.py
import streamlit as st
from generator import generar_script
from evaluator import presence_score, score_response_rhythm
import db
from simulator import simulate_reply
from utils import now_iso
import time
import json

# Inicializar BD
db.init_db()

st.set_page_config(page_title="Presencia Lab — Prototipo", layout="wide")
st.title("Presencia Lab — Prototipo (Entrenamiento de Presencia Masculina Consciente)")

# --- Sidebar: estado y datos del usuario
st.sidebar.header("Tu configuración")
user_identity = st.sidebar.text_input("Identidad corta (para humanización)", "ritmos circadianos / IA social / arte sacro")
if "response_times" not in st.session_state:
    st.session_state.response_times = []
if "conv_id" not in st.session_state:
    st.session_state.conv_id = None
if "scenario_id" not in st.session_state:
    st.session_state.scenario_id = None

# --- Inputs principales
with st.form("scenario_form"):
    st.subheader("Generar nuevo escenario")
    context = st.selectbox("Contexto", ["Cafetería", "Coworking", "Evento social", "Aeropuerto", "Librería"])
    profile = st.selectbox("Perfil de ella", ["Ejecutiva", "Artista", "Intelectual", "Fría distante"])
    state_internal = st.selectbox("Tu estado interno (auto-evalúa)", ["Calmado", "Curioso", "Dominante", "Inseguro"])
    submitted = st.form_submit_button("Generar y simular")

if submitted:
    script_text, meta = generar_script(context, profile, state_internal, user_identity=user_identity)
    # Guardar escenario
    sid = db.save_scenario(context, profile, state_internal, script_text, meta)
    st.session_state.scenario_id = sid
    st.success(f"Escenario guardado (id={sid})")
    st.markdown("### Script generado")
    st.markdown(script_text)
    st.markdown("**Meta / instrucciones**")
    st.json(meta)

    # Iniciar conversación de prueba: el usuario "dice" la apertura y simulamos respuesta
    user_line = meta["strategy"]["piece_templates"]["apertura"]
    conv_user_id = db.append_conversation(sid, "user", user_line)
    st.write("Tu línea (apertura) enviada al simulador.")
    # Simular respuesta de 'ella'
    her_reply, latency = simulate_reply(profile)
    # Simulamos el retraso visual para que entrenes ritmo
    st.write(f"Simulando espera de {latency:.2f} s (observa tu sensación corporal).")
    time.sleep(min(latency, 4.0))  # limitamos a 4s para demo local, pero guardamos latencia real
    conv_her_id = db.append_conversation(sid, "her", her_reply)
    st.write(f"Respuesta simulada ({profile}): {her_reply}")
    # Guardar latencia en session y base
    st.session_state.response_times.append(latency)
    # Guard metric
    db.save_metric(conv_her_id, "latency_seconds", latency)
    # Score provisional
    # extract cierre text
    cierre_text = meta["strategy"]["piece_templates"]["cierre"]
    score = presence_score(state_internal, meta, cierre_text, st.session_state.response_times)
    st.metric("Puntuación de presencia", f"{score} / 100")
    # Guardar entrenamiento diario
    db.save_training(now_iso().split("T")[0], sid, score, notes="auto-test")
    st.info("Entrenamiento guardado en historial.")

# --- Conversación interactiva (modo simulador conversacional con memoria)
st.subheader("Simulador conversacional con memoria")
st.write("Si hay un escenario activo, puedes enviar líneas (tu práctica) y la simulación responderá. El sistema mide latencias y guarda la conversación.")
if st.session_state.scenario_id:
    st.write(f"Escenario activo id={st.session_state.scenario_id}")
    # show recent conv
    recent = db.list_scenarios(10)
    st.markdown("### Historial (últimos escenarios)")
    for sc in recent[:6]:
        st.markdown(f"- id {sc['id']} | {sc['context']} | {sc['profile']} | {sc['created_at']}")

    user_msg = st.text_input("Escribe tu próxima línea práctica (ej. la Pieza 2 o 3)")
    if st.button("Enviar práctica"):
        if not user_msg.strip():
            st.warning("Escribe algo pequeño para probar.")
        else:
            cid = db.append_conversation(st.session_state.scenario_id, "user", user_msg)
            # Simular respuesta
            her_reply, latency = simulate_reply(profile)
            time.sleep(min(latency, 3.5))  # demo
            hid = db.append_conversation(st.session_state.scenario_id, "her", her_reply)
            st.write(f"Her: {her_reply}  (lat: {latency:.2f}s)")
            st.session_state.response_times.append(latency)
            db.save_metric(hid, "latency_seconds", latency)
            # recalcular score usando cierre de último escenario
            sc_meta = recent[0]["meta"] if recent else {}
            cierre_text = sc_meta.get("strategy", {}).get("piece_templates", {}).get("cierre", "")
            score = presence_score(state_internal, sc_meta, cierre_text, st.session_state.response_times)
            st.metric("Puntuación actual", f"{score} / 100")
else:
    st.info("Genera un escenario en el formulario superior para activar la simulación.")

# --- Modo Entrenamiento Diario (resumen)
st.subheader("Modo entrenamiento diario — resumen")
today = now_iso().split("T")[0]
st.write(f"Fecha: {today}")
# traer trainings
trainings = []
conn = None
try:
    trainings = db.list_scenarios(25)  # reusa función para mostrar; para brevity
except Exception:
    trainings = []
st.markdown("Últimos escenarios guardados:")
for t in trainings[:8]:
    st.markdown(f"- id {t['id']} | {t['context']} | {t['profile']} | {t['created_at']}")

# --- Análisis de ritmo de respuesta
st.subheader("Análisis de ritmo de respuesta")
times = st.session_state.response_times
if times:
    import numpy as np
    avg = np.mean(times)
    st.write(f"Respuestas registradas: {len(times)}  — Latencia media: {avg:.2f} s")
    rr_score = score_response_rhythm(times)
    st.progress(int(rr_score*100))
    st.caption("Ideal: 2.0–5.0 s (pausas meditadas y presencia).")
else:
    st.write("No hay latencias registradas aún. Genera interacción para que el sistema mida tu ritmo.")

st.markdown("---")
st.caption("Prototipo — diseñado para entrenar presencia: regulación, polaridad, tensión controlada y vulnerabilidad integrada. Guarda y revisa tu historial para ver evolución.")