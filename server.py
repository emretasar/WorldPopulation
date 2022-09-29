<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template
from datetime import datetime
>>>>>>> 39c08415f98f6334a3c68416f24303eb871c1984
import views


def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page)
<<<<<<< HEAD

    return app

=======

    return app
>>>>>>> 39c08415f98f6334a3c68416f24303eb871c1984

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)
