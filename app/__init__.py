from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloqiu string'
bootstrap = Bootstrap(app)

from app import views
