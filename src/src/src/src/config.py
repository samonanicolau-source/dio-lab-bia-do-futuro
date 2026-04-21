import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DATA_PATH = "data/" # Pasta onde estão seus JSONs e CSVs
