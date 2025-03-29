import random
from flask import Flask, render_template, request
import base64
from openai import OpenAI
import os
import random
from dotenv import load_dotenv


app = Flask(__name__)
category_of_the_day = "animals"
word_of_the_day = "horse"
letter_reveal_order = random.shuffle(list(range(len(word_of_the_day))))


# Frontend routes
@app.route("/")
def welcome():
    params = {"category": category_of_the_day, "letters": "_ " * len(word_of_the_day)}
    return render_template("pages/index.html", **params)


# API routes
@app.route("/api/guess", methods=["POST"])
def guess():
    user_guess = request.form["guess"]
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Describe what is in this image in one word",
                    },
                    {
                        "type": "input_image",
                        "detail": "low",
                        "image_url": f"data:image/jpeg;base64,{user_guess}",
                    },
                ],
            }
        ],
    )
    model_guess = response.output_text.trim().lower()
    params = {
        "guess": model_guess,
        "result": model_guess.lower() == word_of_the_day.lower(),
    }

    return render_template("responses/guess.html", **params)


@app.route("/api/hint", methods=["GET"])
def hint():
    letters = request.form[
        "letters_revealed"
    ]  # add front end validation for only 1 letter left.
    letters = letters.replace(" ", "")
    ar = []
    for char, i in enumerate(letters):
        if char == "_":
            ar.append(i)
    reveal_index = len(random.randint(0, len(ar) - 1))
    letters[reveal_index] = word_of_the_day[reveal_index]
    params = {"category": category_of_the_day, "letters": " ".join(letters)}
    return render_template("pages/index.html", **params)


@app.route("/api/giveup", methods=["GET"])
def giveup():
    params = {"answer": word_of_the_day}
    return render_template("pages/index.html", **params)


@app.route("/api/leaderboard")
def leaderboard():
    # hit the database ORDER_BY hints, guesses, time
    top_ten = []


@app.route("/api/winner")
def winner():
    num_hints = int(
        request.form["num_hints"]
    )  # add front end validation for only 1 letter left.
    num_guesses = int(request.form["guesses"])
    num_seconds = int(request.form["time"])
    name = request.form["name"]

    # write to mongo db everything


# Start with flask web app in debug mode
# TODO: `argparse` for `debug` flag`
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
