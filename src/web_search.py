# src/web_search.py
# Maneja búsquedas web para obtener información

import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_web(query):
    """Realiza una búsqueda en DuckDuckGo y devuelve una respuesta breve."""
    try:
        # Codificar la consulta para la URL
        query = urllib.parse.quote(query)
        url = f"https://html.duckduckgo.com/html/?q={query}"
        
        # Hacer la solicitud con un User-Agent para evitar bloqueos
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        # Parsear el HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Buscar el primer resultado relevante (por ejemplo, un snippet o título)
        result = soup.find("a", class_="result__a")
        if result:
            return result.text.strip()
        
        # Si no hay snippet, buscar en el cuerpo del resultado
        body = soup.find("div", class_="result__snippet")
        if body:
            return body.text.strip()
        
        return "¡Argh! No encontré nada útil en los mares del Internet."
    
    except requests.RequestException as e:
        return f"¡Tormenta en la red! No pude buscar: {str(e)}"