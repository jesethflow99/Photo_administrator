from flask import Flask,render_template,request
from blueprints.user.routes import user
import os
from dotenv import load_dotenv
load_dotenv()
app= Flask(__name__)

app.register_blueprint(user,url_prefix="/user")

app.secret_key=os.getenv("SECRET_KEY")

@app.route("/")
def login():

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")