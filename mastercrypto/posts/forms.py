from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired, url

class RegularPostForm(FlaskForm):
    title = StringField('Título del post:', validators=[DataRequired()])
    subtitle = StringField('Sumario:', validators=[DataRequired()])
    photo_url = StringField("Ingresa la URL de la foto:", validators=[DataRequired(), url()])
    status = SelectField(u'En qué estado se guardará el post:',
                          choices=[('Publicado', 'Publicado'), ('Desactivado', 'Desactivado'),
                                   ('Draft', 'Draft')])
    content = TextAreaField('Escribe el contenido del post:',validators=[DataRequired()] )
    submit = SubmitField('Guardar')

class VideoPostForm(FlaskForm):
    title = StringField('Título del post:', validators=[DataRequired()])
    video_link = StringField("Ingresa la URL de la foto:", validators=[DataRequired(), url()])
    subtitle = StringField('Sumario:', validators=[DataRequired()])
    status = SelectField(u'En qué estado se guardará el video:',
                          choices=[('Publicado', 'Publicado'), ('Desactivado', 'Desactivado')])
    submit = SubmitField('Guardar')
