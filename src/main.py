# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask
# constructor, the path of the correct module
app = Flask(__name__)


# Default route added using a decorator, for view function 'welcome'
# We pass a simple string to the frontend browser
@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/api/guess", methods=["POST"])
def guess():
    return render_template("guess.html", guess=request.form["guess"])


# Start with flask web app, with debug as True,# only if this is the starting page
if __name__ == "__main__":
    app.run(debug=True)
