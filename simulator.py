# simulator.py
import random

def her_response(archetype, tension_level):
    responses = {
        "Rechazo": ["Ahora no puedo hablar, gracias", "Estoy ocupada", "No me interesa"],
        "Neutral": ["Mmh, ¿nos conocemos?", "Interesante observación..."],
        "Invertida": ["¿Y tú quién eres para decirme eso?", "Jaja, qué atrevido"]
    }
    # 20% de probabilidad de rechazo para entrenar tu desapego
    if random.random() < 0.20:
        return random.choice(responses["Rechazo"]), "Baja"
    return random.choice(responses["Neutral"]), "Media"
