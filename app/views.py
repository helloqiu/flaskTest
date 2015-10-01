from app import app
from flask import render_template , request


@app.route('/' , methods=['GET' , 'POST'])
@app.route('/login', methods=['GET' , 'POST'])
def login():
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == 'POST':
		if request.form['username']:
			return 'Success'
		else:
			return 'Fail'
