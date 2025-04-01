from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DIRECTORIO"))

def listar_carpetas():
    lista=os.listdir(os.getenv("DIRECTORIO"))
    return lista

def ver_galeria(username):
    directorio = os.path.join(os.getenv('DIRECTORIO'), username)
    
    # Verifica que el directorio exista antes de intentar listar su contenido
    if not os.path.isdir(directorio):
        return []

    # Obtiene la lista de archivos y filtra solo los que terminen en .jpg (ignora mayúsculas/minúsculas)
    lista = [i for i in os.listdir(directorio) if isinstance(i, str) and i.lower().endswith('.jpg')]
    
    return lista
