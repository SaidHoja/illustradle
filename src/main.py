# import spacy
# import numpy as np

from flask import Flask, render_template, request

print("Initializing Flask...")
app = Flask(__name__)

# model_name = "en_core_web_lg"
# print(f"Initializing spaCy ({model_name})...")
# nlp_en = spacy.load(model_name)

category_of_the_day = "animals"
word_of_the_day = "horse"
# word_of_the_day_nlp = nlp_en(word_of_the_day)


# https://medium.com/data-science/how-to-build-a-fast-most-similar-words-method-in-spacy-32ed104fe498
# def most_similar(in_word: str, topn: int = 5) -> list[str]:
#     word = nlp_en.vocab[in_word]
#     similarities = []
#     for w in nlp_en.vocab.strings:
#         if w.is_lower():
#             similarities.append((w.text, w.similarity(word)))
#     similarities.sort(key=lambda a: a[1], reverse=False)
#     return similarities


# print(f"Computing similar words to {word_of_the_day}...")
# print(most_similar(word_of_the_day), 20)


# def test_word(word: str) -> float:
#     return word_of_the_day_nlp.similarity(nlp_en(word))


# Frontend routes
@app.route("/")
def welcome():
    params = {"category": category_of_the_day, "letters": "_" * len(word_of_the_day)}
    return render_template("pages/index.html", **params)


# API routes
@app.route("/api/guess", methods=["POST"])
def guess():
    user_guess = request.form["guess"]
    # similarity = test_word(request.form["guess"])

    params = {
        "guess": request.form["guess"],
        # "similarity": round(similarity * 100, 2),
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
