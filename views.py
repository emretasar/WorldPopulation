from datetime import datetime
from flask import render_template


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def population_page():
    return render_template("population.html")
