from app import app
from flask import render_template

@app.route("/mood")
def mood():
    return render_template("mood.html")