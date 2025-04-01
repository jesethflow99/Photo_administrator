from flask import Blueprint,render_template,request,flash,redirect,url_for,session,jsonify
import os
from dotenv import load_dotenv
from db import User
from controllers.eventos import ver_galeria
from pathlib import Path

load_dotenv()

user= Blueprint("user",__name__)



@user.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return redirect(url_for("login"))
    if request.method=="POST":
        username=request.form.get("username")
        token=request.form.get("token")
        session["username"]=username
        session["token"]=token
        loged=User.comprobe(username,token)
        if username=="admin" and token==os.getenv("ADMIN_PASSWORD"):
            print("ingresando desde admin")
            return redirect(url_for("admin.index"))
        if loged:
            lista=ver_galeria(username)
            if not lista:
                flash("No tienes fotos en tu galeria")
                return render_template("login.html")
            return render_template("photos.html",username=username,lista=lista,title="Galeria de fotos de "+username) 
        else:
            flash("Usuario o contraseña incorrectos")
            flash("si olvidaste tu contraseña, contacta a Cuve fotogragia Te resolvemos con gusto")
            return redirect(url_for("login"))

@user.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect(url_for("login"))


@user.route("/guardar_seleccion", methods=["POST"])
def guardar_seleccion():
    data = request.get_json()
    seleccionadas = data.get("imagenes", [])

    if not seleccionadas:
        return jsonify({"mensaje": "No se seleccionaron imágenes"}), 400

    print("Imágenes seleccionadas:", seleccionadas)

    with open(f"static/imagenes/{session.get('username')}/seleccion.txt", "w") as f:
        for imagen in seleccionadas:
            f.write(imagen + "\n")

    return jsonify({"mensaje": "Selección guardada con éxito", "imagenes": seleccionadas})
