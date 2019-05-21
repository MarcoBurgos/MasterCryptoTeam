from flask import render_template, request, Blueprint, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from mastercrypto.models import User, generate_password_hash
from mastercrypto import db
from mastercrypto.models import Post, Videopost, User
from mastercrypto.core.forms import UserSignInForm
import datetime
import os
import re

core = Blueprint('core',__name__)

@core.route('/', methods=['GET', 'POST'])
def index():

    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()
    ft_video = Videopost.query.order_by(Videopost.date_posted.desc()).one()


    return render_template('index.html', recent_posts = recent_posts, ft_video = ft_video)

@core.route('/login_consoleMC', methods=['GET', 'POST'])
def login_consoleMC():
    form = UserSignInForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data

        try:
            user_submited = User.query.filter_by(email=email).first()
        except Exception as e:
            abort(500,e)


        if user_submited is None:
            flash(f"Usario no encontrado")

            return redirect(url_for('core.login_consoleMC'))

        else:
            if (user_submited.check_password(password)):
                login_user(user_submited)
                return redirect(url_for('core.dashboard_MC'))

            else:
                flash(f"Contraseña equivocada")

                return redirect(url_for('core.index'))

    return render_template('login.html', form=form)

@core.route('/dashboard_MC', methods=['GET', 'POST'])
def dashboard_MC():

    posts = Post.query.order_by(Post.date_posted.desc()).all()
    videoposts = Videopost.query.order_by(Videopost.date_posted.desc()).all()

    return render_template('dashboard.html', posts=posts, videoposts=videoposts)


@core.route('/blog', methods=['GET', 'POST'])
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('blog.html', posts=posts)
