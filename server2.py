from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template("Home.html", current_year=current_year)



if __name__ == "__main__":
    app.run(port=80,debug=True)
