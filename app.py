# app.py
import streamlit as st
from generator import generate_god_level_script
from evaluator import get_astrological_warning, presence_score
from simulator import her_response

st.set_page_config(page_title="ALPHA-35: Singularity", layout="wide")

st.title("🚀 ALPHA-35: Simulador de Presencia Integral")

# PILAR 1: AUTORREGULACIÓN (Obligatorio)
st.sidebar.header("1. Estado del Sistema Nervioso")
male_state = st.sidebar.selectbox("¿Cómo está tu Hardware interno?", 
                                 ["Regulado", "Curioso", "Dominante", "Escasez", "Abundancia", "Reactivo"])

if male_state in ["Escasez", "Reactivo"]:
    st.warning("ALERTA: Cortisol Alto. Realiza 3 respiraciones exhalando en 8 segundos antes de continuar.")

# PILAR 2 & 3: CONFIGURACIÓN
st.subheader("Configurar Colapso de la Onda")
col1, col2 = st.columns(2)
with col1:
    archetype = st.selectbox("Arquetipo Femenino", ["Ejecutiva", "Artista", "Popular", "Intelectual", "Espiritual", "Fría"])
with col2:
    context = st.selectbox("Contexto Social", ["Funcional", "Social", "Profesional", "Romántico", "Reencuentro"])

if st.button("GENERAR ESTRUCTURA LEGO"):
    exp = generate_god_level_script(male_state, archetype, context)
    
    st.markdown(f"### 🧬 SCRIPT SUGERIDO\n> {exp['script']}")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info(f"**Metacognición:**\n- Emoción: {exp['metacognition']['activa']}\n- Error a evitar: {exp['metacognition']['evitar']}")
    with col_b:
        st.success(f"**Biometría:**\n- Voz: {exp['biological_vars']['voz']}\n- Mirada: {exp['biological_vars']['mirada']}")
    
    st.write(f"🧘 **Sensación Corporal:** {exp['metacognition']['sensacion_corporal']}")

# SIMULACIÓN EN VIVO
st.divider()
st.subheader("💬 Simulador de Respuesta Real")
user_msg = st.text_input("Tú dices:")
if user_msg:
    warnings = get_astrological_warning(user_msg)
    for w in warnings: st.error(w)
    
    resp, tension = her_response(archetype, "Media")
    st.write(f"**Ella ({archetype}):** {resp}")
    
