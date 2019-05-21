from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField)
from wtforms.validators import DataRequired

class UserSignInForm(FlaskForm):
    email = StringField('Dirección de correo electrónico:', validators=[DataRequired()])
    password = StringField('Ingresa tu contraseña:', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')
