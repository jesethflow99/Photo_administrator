from flask import Blueprint,render_template,request,flash,redirect,url_for
import os
from dotenv import load_dotenv
from db import User
from controllers.eventos import ver_galeria
load_dotenv()

user= Blueprint("user",__name__)



@user.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return redirect(url_for("login"))
    if request.method=="POST":
        username=request.form.get("username")
        token=request.form.get("token")
        loged=User.comprobe(username,token)
        if loged:
            lista=ver_galeria(username)
            if not lista:
                flash("No tienes fotos en tu galeria")
                return render_template("login.html")
            return render_template("photos.html",username=username,lista=lista,title="Galeria de fotos de "+username) 
        else:
            flash("Usuario o contraseña incorrectos")
            flash("si olvidaste tu contraseña, contacta a Cuve fotogragia Te resolvemos con gusto")
            return render_template("login.html")
