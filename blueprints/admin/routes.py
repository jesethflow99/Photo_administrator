from flask import Blueprint,render_template,request,flash,redirect,url_for,session
import os
from dotenv import load_dotenv
from db import User
from controllers.eventos import listar_carpetas,ver_galeria
load_dotenv()

admin= Blueprint("admin",__name__)

@admin.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        username=session.get("username")
        token=session.get("token")
        if username == "admin" and token== os.getenv("ADMIN_PASSWORD"):
            lista=User.read()
            return render_template("admin.html",lista=lista if lista else [],title="Panel de administración")
    else:
        return redirect(url_for("cerrar_sesion"))


            
@admin.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect(url_for("login"))


@admin.route("/agregar_usuarios")
def agregar_usuarios():
    if session.get("username")=="admin" and session.get("token")==os.getenv("ADMIN_PASSWORD"):
        lista=listar_carpetas()
        usuarios=User.read()
        print(lista)
        print(usuarios)
        
        usuario = [i[0] for i in usuarios] if usuarios else []

        print(usuario)
        for i in lista:
            if i not in usuario :
                user=User(i)    
                user.create()
        flash("Usuarios creados con éxito")
        return redirect(url_for("admin.index"))
            