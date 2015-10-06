# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request
import getQuestion
import user
from myForm import LoginForm
import sys


reload(sys)
sys.setdefaultencoding('utf8')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    loginForm = LoginForm()
    if request.method == 'GET':
        return render_template("index.html", form=loginForm)
    elif request.method == 'POST':
        if request.form['username']:
            if user.login(request.form['username'], request.form['password']):
                return user_dash_view()
            else:
                return render_template("index.html", error=True, form=loginForm)
        else:
            return 'Fail'


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        if request.form['password'] != request.form['password-repeat']:
            return render_template('register.html', error='passwords are not same')
        else:
            if user.register(request.form['username'], request.form['password']):
                return 'success'
            else:
                return render_template('register.html', error='the username has been registered')


@app.route('/user_dash', methods=['GET', 'POST'])
def user_dash_view():
    data = user.rank()
    if request.method == 'GET':
        return render_template('user_dashboard.html', users=data)
    if request.method == 'POST':
        return render_template('user_dashboard.html', users=data)


@app.route('/question/<int:kind>', methods=['GET', 'POST'])
def question(kind):
    data = getQuestion.get_question('%d' % kind)
    if request.method == 'GET':
        return render_template('question_list.html', question_kind='题目' + '%d' % kind, questions=data, kind=kind)


@app.route('/question/id/<int:id>', methods=['GET', 'POST'])
def show_questions(id):
    data = getQuestion.get_question('', False, '%d' % id)
    if request.method == 'GET':
        return render_template('question.html', question_title=data[0], question_content=data[1], kind=data[3])
    if request.method == 'POST':
        if user.login(request.form['username'], request.form['password']):
            if data[2] != unicode(request.form['answer']):
                return render_template('question.html', question_title=data[0], question_content=data[1], kind=data[3], error=True)
            else:
                user.add_score(request.form['username'], data[4])
                return render_template('question.html', question_title=data[0], question_content=data[1], kind=data[3], success=True)
        else:
            return render_template('question.html', question_title=data[0], question_content=data[1], kind=data[3], loginError=True)
