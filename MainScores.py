from flask import Flask, render_template
from Utils import bad_return_code


def score_server():
    app = Flask(__name__)
    @app.route("/")
    def score_page():
        try:
            file = open("Scores.txt", "r")
            test = file.read()
            return render_template("scores_html.html", SCORE=test)
        except:
            return render_template("scores_html.html", SCORE=bad_return_code)
    if __name__ == "__main__":
        app.run()


score_server()


