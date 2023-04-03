from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world from render.com!</p>"

@app.route("/timeline")
def timeline():
    # ここをInstagram対応させられないか
    return render_template("timeline.html", tag="iosdc")