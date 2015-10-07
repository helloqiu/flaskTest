from flask import Flask
from flask.ext.bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloqiu string'
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    #os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
bootstrap = Bootstrap(app)

from app import views
