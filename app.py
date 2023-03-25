from flask import Flask, url_for, render_template, request
import sys
from os import path
from package import transration

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('index.html', name=name)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    transration.transrate()
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('do_the_login')
        # do_the_login()
    else:
        print('show_the_login_form')
        # show_the_login_form()

if __name__ == '__main__':
    app.run(host='0.0.0.0')