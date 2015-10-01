from app import app
from flask import render_template request


@app.route('/')
@app.route('/login',method=['GET' , 'POST'])
def login():
	if request.method == 'GET':
		return render_template("test.html")
	elif request.method == 'POST':
		
