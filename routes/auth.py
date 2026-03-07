from flask import render_template, request, redirect, url_for, session
from app import app, db, User

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")

        user = User.query.filter_by(email=email).first()

        if user:
            session["user_id"] = user.id
            return redirect(url_for("home"))
        
        return "User not found."
    return render_template("login.html")