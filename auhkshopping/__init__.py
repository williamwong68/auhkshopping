# immport flask from the flask package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()
app = Flask (__name__)

# create a function that creates aa web application
# a web server will run this web application
def create_app():
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'

    # set the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auhkshopping.sqlite'

    # initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    from . import views
    app.register_blueprint(views.bp)

    return app


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")

@app.errorhandler(505)
def internal_error(e):
    return render_template("500.html")

