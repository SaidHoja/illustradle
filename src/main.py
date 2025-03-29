import random
from flask import Flask, render_template, request

app = Flask(__name__)

category_of_the_day = "animals"
word_of_the_day = "horse"
letter_reveal_order = random.shuffle(list(range(len(word_of_the_day))))


# Frontend routes
@app.route("/")
def welcome():
    params = {"category": category_of_the_day, "letters": "_" * len(word_of_the_day)}
    return render_template("pages/index.html", **params)


# API routes
@app.route("/api/guess", methods=["POST"])
def guess():
    user_guess = request.form["guess"]
    params = {
        "guess": request.form["guess"],
    }
    return render_template("responses/guess.html", **params)


@app.route("/api/hint", methods=["GET"])
def hint():
    user_best_guess = request.args.get("best_guess")
    # Do lookup on `user_guess` and find the next best one
    better_guess = "pig"

    params = {"guess": better_guess, "letters": "_o___"}
    return render_template("responses/hint.html", **params)


# Start with flask web app in debug mode
# TODO: `argparse` for `debug` flag`
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
