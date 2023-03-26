from flask import Flask, render_template, request, jsonify, make_response
import sys
from os import path
from package import transration
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    videoUrl = data['video-url']
    print('videoUrl: ' + videoUrl)
    transrate = transration.transrate(videoUrl)
    print('transrate: ' + transrate)

    response = make_response(jsonify(transrate))
    response.headers["Content-Type"] = "application/json"
    return response

    # return jsonify(transrate)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     transration.transrate()
#     return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')