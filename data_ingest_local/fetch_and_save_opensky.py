import os
import json
from datetime import datetime
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))  # 👈 Esto es clave

from src.api_client import fetch_opensky_states

def save_raw_data_to_file():
    try:
        # Obtener datos desde la API de OpenSky
        data = fetch_opensky_states()

        # Crear carpeta si no existe
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)

        # Nombre de archivo con fecha
        timestamp = datetime.utcnow().strftime("%Y%m%d")
        filename = f"opensky_raw_{timestamp}.json"
        filepath = data_dir / filename

        # Guardar archivo JSON
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

        print(f"✅ Datos guardados en: {filepath}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    save_raw_data_to_file()
