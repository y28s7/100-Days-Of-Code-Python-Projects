from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def bold(function):
    def wrapper(*args, **kwargs):
        return "<strong>" + function() + "</strong>"
    return wrapper


def underline(function):
    def wrapper(*args, **kwargs):
        return "<u>" + function() + "</u>"
    return wrapper


def italicize(function):
    def wrapper(*args, **kwargs):
        return "<em>" + function() + "</em>"
    return wrapper


@app.route("/")
@bold
@underline
@italicize
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<p>This here is a paragraph</p>" \
           '<iframe src="https://giphy.com/embed/26tn33aiTi1jkl6H6" width="480" height="270" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'


@app.route('/bye')
def say_bye():
    return "<p>Bye</p>"


@app.route("/<name>")
def greet(name):
    return f"<p>Hello there {escape(name)}!</p>"


# To start server (in terminal):
# flask --app <filename> run
# To start server (using code):
if __name__ == "__main__":
    app.run(debug=True)
