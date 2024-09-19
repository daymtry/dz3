
from flask import Flask, render_template

import random


app = Flask(__name__)


max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "score": 100},
  {"name": "Sviatoslav", "score": 99},
  {"name": "Юстин", "score": 100},
  {"name": "Viktor", "score": 79},
  {"name": "Ярослав", "score": 93},
]


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
     
    

    pizzas = [
    {"name": "Пепероні", "price": 22, "ingredients": "ковбаса 'Пепероні', сир, соус"},
    {"name": "Пепероні", "price": 29, "ingredients": "ковбаса 'Пепероні', сир, соус"},
    {"name": "Моцарела", "price": 20, "ingredients": "сир 'Моцарела', соус, петрушка"},
    {"name": "Чотири сира", "price": 30, "ingredients": "сир 'Моцарела', сир 'Чедер', сир 'Солугуні', сир 'Брю'"}
    ]
    context = {
    "pizzas": pizzas,
    "title": "Мега меню"
    }
    return render_template("pizzas.html", **context)
if __name__ == "__main__":
    app.run()