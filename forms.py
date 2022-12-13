from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add a Puppy')

class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to Remove:")
    submit = SubmitField("Remove puppy")

class OwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    pup_id = IntegerField('ID of Puppy:')
    submit = SubmitField('Add Owner')