import spacy
import numpy as np

from flask import Flask, render_template, request

print("Initializing Flask...")
app = Flask(__name__)

print("Initializing spaCy...")
nlp_en = spacy.load("en_core_web_md")

category_of_the_day = "animals"
word_of_the_day = "horse"
word_of_the_day_nlp = nlp_en(word_of_the_day)


# https://medium.com/data-science/how-to-build-a-fast-most-similar-words-method-in-spacy-32ed104fe498
def most_similar(word, topn=5):
    word = nlp_en.vocab[str(word)]
    queries = [
        w
        for w in word.vocab
        if w.is_lower == word.is_lower and w.prob >= -15 and np.count_nonzero(w.vector)
    ]

    by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
    return [
        (w.lower_, w.similarity(word))
        for w in by_similarity[: topn + 1]
        if w.lower_ != word.lower_
    ]


print(f"Computing similar words to {word_of_the_day}...")
most_similar_words = most_similar(word_of_the_day, topn=20)
print(most_similar_words)


def test_word(word: str) -> float:
    return word_of_the_day_nlp.similarity(nlp_en(word))


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
    app.run(debug=True, port=8000)
