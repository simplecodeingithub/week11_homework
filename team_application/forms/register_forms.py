# Import FlaskForm class from flask_wtf module or a flask extension
# Import fields from wtforms,used to create forms and (fields are like class attributes).
# Import validation rule

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email

# Create a form class
class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add Name')