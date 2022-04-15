from flask import Flask, request, jsonify, render_template, url_for, redirect, session
from flask_cors import CORS
from src import *
from platform import platform
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisscreetkey2022"
CORS(app)

@app.route("/", methods=["POST","GET"])
def index():
    if "username" in session:
        return redirect(url_for('success_req'))
    else:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            if username =="admin" and password =="hudaxcode":
                session['username'] = username 
                return redirect(url_for('success_req'))
            else:
                return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/logout")
def logout():
    if "username" not in session:
        return redirect(url_for('index'))
    if "username" in session:
        session.pop("username")
        return redirect(url_for('index'))

@app.route("/admin")
def success_req():
    if "username" in session:
        text = "Anda Success Login"
        return render_template("admin.html")
    else:
        return redirect(url_for('index'))

@app.route("/api/license")
def key():
    if request.method == "GET":
        arg = request.args
        device = arg["device"]
        result= license(device)
        return jsonify(result)

@app.route("/api/facebook/publik")
def id_publik():
    if request.method == "GET":
        arg = request.args
        if "id" or "token" in arg:
            id = arg["id"]
            token = arg["token"]
            result = publik(id,token)
            return jsonify(result)

@app.route("/api/facebook/login")
def metodelogin():
    if request.method == "GET":
        arg = request.args
        if arg:
            if "username" or "password" in arg:
                user = arg["username"]
                pasw = arg["password"]
                result = login(user,pasw)
                return jsonify(result)
        return jsonify({"error": "query is required"})
    else:
        return jsonify({"message": "Hello from my server"})


app.run(debug=True)
