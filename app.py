from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    result = 1 + 1
    return render_template('./index.html', calc_result = result)
