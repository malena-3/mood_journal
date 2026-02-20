from app import app
from flask import render_template, request

@app.route("/mood")
def mood():
    return render_template("mood.html")

@app.route("/submit_selection", methods=["POST"])
def submit_selection():
    if request.method == "POST":
        # to get the value of the selected option using its 'name' attribute
        selected_value = request.form.get("moods")

        # can now use the 'selected_value' in your Python logic
        print("selected value:", selected_value)
        # return f"The selected value is: {selected_value}"
        return render_template("new_mood.html", mood=selected_value)