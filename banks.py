# banks.py

MALE_STATES = {
    "Regulado": "Sistema nervioso en calma, tono vagal alto, presencia absoluta.",
    "Curioso": "Interés genuino por el fenómeno, sin hambre de resultado.",
    "Dominante": "Control del espacio y el tiempo, asertividad sin agresión.",
    "Escasez": "Necesidad de validación (Estado a evitar/entrenar).",
    "Abundancia": "Sentimiento de que ya lo tienes todo, ella es solo un plus.",
    "Reactivo": "Defensivo o buscando impresionar (Estado a evitar)."
}

FEMALE_ARCHETYPES = {
    "Ejecutiva": {"rasgo": "Estructura/Poder", "contraste": "Caos emocional oculto"},
    "Artista": {"rasgo": "Caos creativo", "contraste": "Necesidad de anclaje/orden"},
    "Popular": {"rasgo": "Validación externa", "contraste": "Soledad en la cima"},
    "Intelectual": {"rasgo": "Análisis lógico", "contraste": "Hambre de sentir sin pensar"},
    "Espiritual": {"rasgo": "Sensibilidad", "contraste": "Miedo a la crudeza real"},
    "Fría": {"rasgo": "Distancia/Muro", "contraste": "Niña traviesa protegida"}
}

CONTEXTS = ["Funcional (Gym/Super)", "Social (Bar/Fiesta)", "Profesional", "Romántico Previo", "Reencuentro"]

# PIEZAS LEGO (100+ posibilidades por banco)
OBSERVATIONS = [
    "Caminas como si estuvieras huyendo de una idea brillante",
    "Tienes esa mirada de quien ya sabe el final de la película",
    "Parece que estás en una misión secreta entre pasillos"
]

CONTRASTS = [
    "pareces {externo}, pero tu energía dice {interno}",
    "proyectas {externo}, aunque sospecho que tu {interno} es tu verdadero refugio"
]

LIMITS = [
    "Me encanta eso, pero si eres así de {riesgo} siempre, seríamos un desastre",
    "Es fascinante, lástima que parezcas tan problemática a largo plazo"
]

HUMANIZATION = [
    "A veces me pierdo en mis proyectos de {proyecto} y olvido cómo se siente el mundo real. Gracias por el reset.",
    "Mi mente suele analizar patrones de {proyecto}, pero tu cara me acaba de desconfigurar el sistema."
]
