from datetime import datetime
from flask import render_template


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def movies_page():
<<<<<<< HEAD
    return render_template("movies.html")
=======
    return render_template("movies.html")
>>>>>>> 39c08415f98f6334a3c68416f24303eb871c1984
