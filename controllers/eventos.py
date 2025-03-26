from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DIRECTORIO"))

def ver_galeria(username):
    lista=os.listdir(f"{os.getenv("DIRECTORIO")}/{username}")
    return lista

