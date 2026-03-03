# simulator.py
import time
import random
from utils import now_iso
from db import append_conversation, save_metric  # careful: we'll import functions, but to avoid cyclic import app will call directly

# We'll provide a local simple generator for "her" replies.
HER_TEMPLATES = {
    "Ejecutiva": [
        "Interesante punto. No suelo sorprenderme tan fácil.",
        "Me gusta la observación, pero ¿por qué lo dices?",
        "No sé si estoy de acuerdo, suena un poco analítico."
    ],
    "Artista": [
        "Me gusta que lo veas así, tiene otro sentido.",
        "Jaja, me haces reír. No soy tan ordenada.",
        "Eso suena profundo. ¿Y tú qué opinas?"
    ],
    "Intelectual": [
        "Esa lectura es aguda, ¿tienes evidencia?",
        "Me interesa la idea, explícate un poco más.",
        "Prefiero argumentos claros antes que lecturas psicológicas."
    ],
    "Fría distante": [
        "Mmh.",
        "No necesito que me analicen.",
        "Si eso te divierte, bien."
    ]
}

def simulate_reply(profile_label):
    # Simula latencia (segundos)
    latency = random.uniform(1.0, 5.5)
    # Escoge respuesta
    choices = HER_TEMPLATES.get(profile_label, HER_TEMPLATES["Intelectual"])
    reply = random.choice(choices)
    return reply, latency
