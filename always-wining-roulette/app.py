import json
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from datetime import datetime

# Initialize Flask
app = Flask(__name__)

# Initialize SQL_Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Casino.db"
db = SQLAlchemy(app)

# Initialize Alembic
alembic = Alembic()
alembic.init_app(app)


def get_result():
    with open("results-holder.json", "r") as f:
        result = json.load(f)
        return result


result = get_result()


class Roulette(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    try_number = db.Column(db.Integer, unique=True, nullable=False)
    black_counter = db.Column(db.Integer, nullable=False)
    red_counter = db.Column(db.Integer, nullable=False)
    green_counter = db.Column(db.Integer, nullable=False)
    final_bet_money = db.Column(db.Integer, nullable=False)
    final_bet_turn = db.Column(db.Integer, nullable=False)
    lowest_player_wallet = db.Column(db.Integer, nullable=False)
    total_spent = db.Column(db.Integer, nullable=False)
    won_amount = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    update_time = db.Column(db.DateTime, nullable=True, onupdate=datetime.now())

    def __str__(self):
        return f"Try: {str(self.try_number)}"

    def __repr__(self):
        ...


db.create_all()


@app.route("/fill_database/")
def fill_database():
    for summary in result:
        res = Roulette(**summary)
        db.session.add(res)
    db.session.commit()
    return "Success"




