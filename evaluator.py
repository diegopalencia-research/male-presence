# evaluator.py

def get_astrological_warning(user_input):
    # Basado en Mercurio oposición Plutón y Venus cuadratura Saturno
    warnings = []
    if len(user_input.split()) > 30: 
        warnings.append("⚠️ Alerta Mercurio-Pluto: Estás sobre-explicando. Menos es más.") [cite: 346]
    if "quiero" in user_input or "necesito" in user_input:
        warnings.append("⚠️ Alerta Venus-Saturn: Detectada búsqueda de validación por miedo a la insuficiencia.") [cite: 365]
    return warnings

def presence_score(data):
    # Lógica de puntuación basada en la autorregulación vagal
    score = 100
    if data['internal_state'] in ['Escasez', 'Reactivo']: score -= 40
    return score
