from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates', static_folder='../assets', static_url_path='/assets')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:123456@localhost:3306/boss_zp'
app.config['secret_key'] = 'dd06be55a06c03312b2ab109b5f8f6ab'
login_manager = LoginManager(app)

db = SQLAlchemy(app)
from routes import admin_routes
from routes import user_routes