from flask import Blueprint,render_template,request,flash
import os
from dotenv import load_dotenv
from db import User
from controllers.eventos import ver_galeria
load_dotenv()

user= Blueprint("user",__name__)

@user.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        username=request.form.get("username")
        token=request.form.get("token")
        loged=User.comprobe(username,token)
        if loged:
            lista=ver_galeria(username)
            dir=f"{os.getenv('DIRECTORIO')}/{username}"
            return render_template("photos.html",username=username,lista=lista,dir=dir)
        else:
            flash("Usuario o contraseña incorrectos")
            flash("si olvidaste tu contraseña, contacta a Cuve fotogragia Te resolvemos con gusto")
            return render_template("login.html")
