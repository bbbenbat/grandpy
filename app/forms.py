from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SendMessage(FlaskForm):
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField('Dis moi GrandPy...')
