from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from .models import User

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

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')
    
class Login(FlaskForm):
    """
    - email -> Cant be empty; true address
    - password -> Cant be empty or simple; verify password 
    """
    email = StringField('ਈ-ਮੇਲ / Email', validators=[DataRequired(), Email()])
    password = PasswordField('ਪਾਸਵਰਡ / Password', validators=[DataRequired()])
    submit = SubmitField('Login')








