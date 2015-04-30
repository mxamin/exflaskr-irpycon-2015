from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length


class EntryForm(Form):
    title = StringField('Title', validators=[
        DataRequired(),
        Length(1, 64)
    ])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Add')
