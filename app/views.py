# -*- coding: utf-8 -*-
from app import app
from flask import render_template , request
import login
import register
import rank

@app.route('/' , methods=['GET' , 'POST'])
@app.route('/login', methods=['GET' , 'POST'])
def login_view():
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == 'POST':
		if request.form['username']:
			if login.login(request.form['username'] , request.form['password']):
				return 'success'
			else:
				return 'fail'
		else:
			return 'Fail'
@app.route('/register', methods=['GET' , 'POST'])
def register_view():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		if request.form['password'] != request.form['password-repeat']:
			return render_template('register.html' , error='passwords are not same')
		else:
			if register.register(request.form['username'] , request.form['password']):
				return 'success'
			else:
				return render_template('register.html' , error='the username has been registered')

@app.route('/user_dash', methods=['GET' , 'POST'])
def user_dash_view():
	data=rank.rank()
	if request.method == 'GET':
		return render_template('user_dashboard.html' , users=data)