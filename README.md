# Chatbot Pirata

Un chatbot temático de consola en Python que simula un pirata parlanchín llamado Capitán Grok Sparrow. Responde a frases predefinidas con jerga pirata y puede buscar información en Internet para responder preguntas.

## Requisitos
- Python 3.6 o superior
- Dependencias: `requests`, `beautifulsoup4`

## Instalación
1. Clona el repositorio o copia los archivos.
2. Crea un entorno virtual (opcional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instala las dependencias: 
    ```bash
    pip install -r requirements.txt
4. Ejecuta el chatbot: 
    ```bash
    python main.py

## Uso

- Escribe mensajes como "hola", "chiste", "nombre" o "salir".
- Haz preguntas con "?" (ejemplo: "¿Cuál es la capital de Francia?") para buscar en Internet.
- Usa "salir" para terminar la conversación.

## Estructura

- src/: Código fuente (chatbot.py, responses.py, web_search.py).
- data/: Logs y datos.
- main.py: Punto de entrada

## Futuras mejoras 

- Guardar conversaciones en data/conversation.log.
- Usar una API de búsqueda más robusta (como SerpAPI).
- Interfaz gráfica con tkinter.