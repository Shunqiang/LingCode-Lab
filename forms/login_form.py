from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(label='YONGHUMING', validators=[DataRequired()])
    password = PasswordField(label='PW', validators=[DataRequired()])
    submit = SubmitField('Login')