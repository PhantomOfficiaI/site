from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddNoteForm(FlaskForm):
    text = TextAreaField('Write here something', validators=[DataRequired()])
    submit = SubmitField('Ok')