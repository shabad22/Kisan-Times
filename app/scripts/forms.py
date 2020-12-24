from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class Register(FlaskForm):
    """
    - username -> Cant be empty; length
    - email -> Cant be empty; true address
    - password -> Cant be empty or simple 
    """
    username = StringField('ਨਾਮ / Username', validators=[DataRequired(), Length(min=4, max=10)])
    email = EmailField('ਈ-ਮੇਲ / Email', validators=[DataRequired(), Email()])
    password = PasswordField('ਪਾਸਵਰਡ / Password', validators=[DataRequired()])
    submit = SubmitField('Join Us')

class Login(FlaskForm):
    """
    - email -> Cant be empty; true address
    - password -> Cant be empty or simple; verify password 
    """
    email = StringField('ਈ-ਮੇਲ / Email', validators=[DataRequired(), Email()])
    password = PasswordField('ਪਾਸਵਰਡ / Password', validators=[DataRequired()])
    submit = SubmitField('Login')








