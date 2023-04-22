from flask import Flask, render_template, request, jsonify, make_response
import sys
from os import path
from package import transration
from flask_cors import CORS
from package.emailSend import send_email
from package.openaiApi import openaiApiFunc
import json
from googletrans import Translator

app = Flask(__name__)
app.debug = True
CORS(app)
translator = Translator()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    videoUrl = data['videoUrl']
    email = data['email']
    languages = data['languages']
    print('data: ' + str(data))
    print('videoUrl: ' + videoUrl)
    print('email: ' + email)
    print('languages: ' + str(languages))
    # transrate = transration.transrate(data)
    # transrate_split = transrate.split(',')
    # print('transrate: ', transrate)
    result_list = []
    
    print(translator.translate('안녕하세여', dest='en').text)
    # result_list.append(result_list)
    # print('transrate_split: ' , transrate_split)
    # for t in transrate:
    #     print('번역: ' + translator.translate(t, src='ko', dest='en'))
    #     result_list.append(translator.translate(t, src='ko', dest='en'))
    # # transrate_result = openaiApiFunc(transrate, str(languages))
    # print('result_list: ' + result_list)

    # response = make_response(jsonify(transrate))
    # response.headers["Content-Type"] = "application/json"

    # # 이메일 보내기
    # # 보내는 사람, 받는 사람, 제목, 내용, 첨부파일 경로 지정
    # sender_email = "soon9086@gmail.com"
    # receiver_email = "soon9086@gmail.com"
    # subject = "Email Subject"
    # body = "Email Body"
    # filename = "attachment.txt"

    # is_sent = send_email(sender_email, receiver_email, subject, body, filename)

    # if is_sent:
    #     print("Email sent successfully.")
    # else:
    #     print("Failed to send email.")

    return True

    # return jsonify(transrate)

@app.route('/api/openai', methods=['POST'])
def openai():
    data = request.get_json()
    # print('data: ' + data)
    msg = data['massege']
    languages = str(data['languages'])
    print('languages: ' + languages)
    result = openaiApiFunc(msg, languages)
    print('result: ' + result)
    
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
