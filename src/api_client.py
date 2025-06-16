import requests
import json
from typing import Dict, Any


def fetch_opensky_states() -> Dict[str, Any]:
    """
    Llama a la API pública de OpenSky para obtener el estado actual de todos los vuelos.
    Returns:
        dict: Respuesta JSON con la clave 'states'.
    """
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    return response.json()
