from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "supersecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/mood_journal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize the database
db = SQLAlchemy(app)

#create db model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    entries = db.relationship("Entry", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.id} - {self.name}>"

class Entry(db.Model):
    __tablename__ = "entries"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    mood = db.Column(db.String(50), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    #create function to return a string when we add something
    def __repr__(self):
        return f"<Entry {self.id} - {self.text}>"

import routes

print(app.url_map)

if __name__ == "__main__":
    app.run(debug = True)

