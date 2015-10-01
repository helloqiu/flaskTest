from app import app
from flask import render_template , request
import login

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
	return render_template('register.html')