# src/chatbot.py
# Lógica principal del chatbot

from .responses import get_response

def run_chatbot():
    """Ejecuta el bucle de conversación del chatbot."""
    print("¡Bienvenido a bordo! Soy el Capitán Grok Sparrow. Escribe algo o di 'salir' para zarpar.")
    
    while True:
        # Lee el mensaje del usuario
        user_input = input("Tú: ")
        
        # Obtiene la respuesta
        response = get_response(user_input)
        
        # Muestra la respuesta
        print(f"Capitán Grok Sparrow: {response}")
        
        # Termina si el usuario escribe "salir"
        if "salir" in user_input.lower():
            break