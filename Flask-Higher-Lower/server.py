from flask import Flask
from random import randint

app = Flask(__name__)
correct_number = randint(0, 9)


def center(function):
    def wrapper():
        return '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' + function() \
            + "</div>"
    return wrapper


@app.route("/")
@center
def home_page():
    print(correct_number)
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<iframe src="https://giphy.com/embed/VxHslc0YBJqAXGaaZ7" width="480" height="329" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'


@app.route("/<int:guess>")
def guess_check(guess):
    if guess < correct_number:
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">Too Low!</h1>' \
                 '<iframe src="https://giphy.com/embed/bTDZ6bD6TBPTrg1JAq" width="480" height="269" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    elif guess > correct_number:
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">Too High!</h1>' \
                 '<iframe src="https://giphy.com/embed/jbRrS0VBGPn0VOEbY5" width="480" height="400" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    else:
        result = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%, -60%);">' \
                 '<h1 style="text-align:center;">You Got It!</h1>' \
                 '<iframe src="https://giphy.com/embed/byIG2EjdYd7ViOH6IF" width="480" height="216" frameBorder="0" ' \
                 'class="giphy-embed" allowFullScreen></iframe>' \
                 '</div>'
    return result


# To start server (in terminal):
# flask --app <filename> run
# To start server (using code):
if __name__ == "__main__":
    app.run(debug=True)
