# src/responses.py
# Maneja las respuestas del chatbot basadas en palabras clave y búsqueda web

from .web_search import search_web

def get_response(message):
    """Devuelve una respuesta basada en el mensaje del usuario."""
    message = message.lower().strip()
    
    # Diccionario de respuestas predefinidas
    responses = {
        "hola": "¡Argh! Saludos, marinero. ¿Qué tesoro buscas hoy?",
        "cómo estás": "¡Más firme que un mástil en tormenta, camarada!",
        "nombre": "Soy el Capitán Grok Sparrow, el más astuto de los siete mares.",
        "ayuda": "¡Echa el ancla! Dime qué necesitas, grumete.",
        "tesoro": "¡Ja! El tesoro está donde el mapa no miente. ¿Tienes uno?",
        "chiste": "¡Escucha! ¿Por qué el pirata rompió con su pareja? ¡Porque era un amor a la deriva!",
        "salir": "¡Izad velas! Hasta la próxima, marinero."
    }
    
    # Respuestas predefinidas
    for key, response in responses.items():
        if key in message:
            return response
    
    # Detectar preguntas que requieran búsqueda web (contienen "¿")
    if "?" in message:
        # Extraer la parte de la pregunta (sin el "¿")
        query = message.replace("¿", "").strip()
        web_result = search_web(query)
        return f"¡Ojo al catalejo! Esto encontré en los mares del saber: {web_result}"
    
    # Respuesta por defecto
    return "¡Arf! No entiendo tu parloteo. Habla claro, marinero."