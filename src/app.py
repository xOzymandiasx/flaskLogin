from flask import Flask, render_template, request, redirect, url_for, flash;
from config import config;
import sqlite3;
import os;

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

app = Flask(__name__);

@app.route("/")
def index():
  return render_template("/index.html");

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    usuario = request.form["username"];
    password = request.form["password"];
    with sqlite3.connect(DATABASE) as con:
      cur = con.cursor();
      query = "SELECT * FROM personas WHERE usuario = ?";
      cur.execute(query, (usuario,));
      users = cur.fetchone();
      if users:
        if users[1] == password:
          return redirect(url_for("home", usuario=users[2]));
        else:
          flash("Incorrect password");
          return render_template("auth/login.html");
      else:
        flash("User not found");
        return render_template("auth/login.html");
  else:
    return render_template('auth/login.html');

@app.route("/home") 
def home():
  usuario = request.args.get("usuario");
  return render_template("home.html", usuario=usuario);

if __name__ == "__main__":
  app.config.from_object(config["development"]);
  app.secret_key = '12345';
  app.run();

