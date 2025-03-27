from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DIRECTORIO"))

def listar_carpetas():
    lista=os.listdir(os.getenv("DIRECTORIO"))
    return lista

def ver_galeria(username):
    lista=os.listdir(f"{os.getenv('DIRECTORIO')}/{username}")
    filtro=["seleccion.txt"]
    lista=[i for i in lista if i not in filtro]
    return lista

