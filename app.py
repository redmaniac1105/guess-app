from flask import Flask, render_template, request
import math
import random

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello_world():
    return render_template("index.html")

@app.route("/lottery", methods=['POST'])
def lottery():
    n = request.form['num']
    lucky = math.floor(random.random()*100)
    print(lucky)
    if (n == lucky):
        return "<body style='background-color:black'><p style ='color:white; font-size:large;'>Hurray on Winning Lottery</p></body>"
    else:
        return "<body style='background-color:black'><p style ='color:white; font-size:large;'>Better luck next time</p></body>"


if __name__ == "__main__":
    app.run()