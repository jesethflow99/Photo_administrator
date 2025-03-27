from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DIRECTORIO"))

def listar_carpetas():
    lista=os.listdir(os.getenv("DIRECTORIO"))
    return lista

def ver_galeria(username):
    lista=os.listdir(f"{os.getenv('DIRECTORIO')}/{username}")
    return lista

