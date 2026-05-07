from dotenv import load_dotenv
import os

# Carga variables del archivo .env
load_dotenv()

database = os.getenv("DATABASE_URL")
debug = os.getenv("DEBUG")
env = os.getenv("produccion")

print(f"Base de datos: {database}")
print(f"Modo debug: {debug}")
print(f"Entorno: {env}")
print(os.getenv("API_KEY"))
print("configuracion cargada correctamente")

