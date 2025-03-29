import spacy

from flask import Flask, render_template, request

print("Initializing Flask...")
app = Flask(__name__)

print("Initializing spaCy...")
nlp = spacy.load("en_core_web_lg")

category_of_the_day = "animals"
word_of_the_day = "horse"
word_of_the_day_nlp = nlp(word_of_the_day)


def test_word(word: str) -> float:
    return word_of_the_day_nlp.similarity(nlp(word))


# Frontend routes
@app.route("/")
def welcome():
    params = {"category": category_of_the_day, "letters": "_" * len(word_of_the_day)}
    return render_template("pages/index.html", **params)


# API routes
@app.route("/api/guess", methods=["POST"])
def guess():
    user_guess = request.form["guess"]

    similarity = test_word(request.form["guess"])

    print(similarity)

    params = {
        "guess": request.form["guess"],
        "similarity": round(similarity * 100, 2),
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
    app.run(debug=True)
