from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DeleteArticleForm(FlaskForm):
    article_id = HiddenField(label='标题', validators=[DataRequired()])
    submit = SubmitField(label='删除')