from flask.ext.wtf import Form
from wtforms.validators import Required, Length, EqualTo
from wtforms import TextField, BooleanField, PasswordField

class LoginForm(Form):
    login = TextField('Spotify login', validators = [Required()])
    password = PasswordField('New Password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)