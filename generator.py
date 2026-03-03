# generator.py
import random
import banks

def generate_god_level_script(male_state, archetype, context):
    arch = banks.FEMALE_ARCHETYPES[archetype]
    
    # Ensamblaje Estructural
    apertura = random.choice(banks.OBSERVATIONS)
    lectura = random.choice(banks.CONTRASTS).format(
        externo=arch["rasgo"], interno=arch["contraste"]
    )
    tension = random.choice(banks.LIMITS).format(riesgo=arch["rasgo"].lower())
    cierre = random.choice(banks.HUMANIZATION).format(proyecto="IA social / Aeroespacial")

    return {
        "script": f"{apertura}. {lectura}. {tension}. {cierre}",
        "metacognition": {
            "activa": "Curiosidad + Desafío Leve",
            "evitar": "Sonar confrontativo o controlador (Mercurio-Pluto)",
            "sensacion_corporal": "Pecho abierto, mandíbula relajada, ritmo lento",
            "vagal_check": "¿Estás respirando desde el diafragma o desde el pecho?"
        },
        "biological_vars": {
            "voz": "Bajar un octavo, pausas de 1.5s entre frases",
            "mirada": "3-5 segundos, luego retirar lentamente",
            "proximidad": "Respetar el espacio, pero no retroceder"
        }
    }
