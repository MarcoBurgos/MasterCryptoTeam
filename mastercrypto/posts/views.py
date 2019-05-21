from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint, abort
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from mastercrypto import db
from mastercrypto.models import Post, Videopost
from mastercrypto.posts.forms import RegularPostForm, VideoPostForm
from datetime import datetime

posts = Blueprint('posts', __name__)


@posts.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = RegularPostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data,
                            subtitle = form.subtitle.data,
                            photo_url = form.photo_url.data,
                            date_posted = datetime.now(),
                            content = form.content.data,
                            status =  form.status.data,
                            user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        flash(f"Creaste un post, id: {post.id}, título: {post.title}")
        return redirect(url_for('core.dashboard_MC'))

    return render_template('create_post.html', form=form)


@posts.route('/create_videopost', methods=['GET', 'POST'])
# @login_required
def create_videopost():
    form = VideoPostForm()
    if form.validate_on_submit():
        videopost = Videopost(title = form.title.data,
                            subtitle = form.subtitle.data,
                            video_link = form.video_link.data,
                            date_posted = datetime.now(),
                            status =  form.status.data,
                            user_id = 1)
        db.session.add(videopost)
        db.session.commit()
        flash(f"Creaste un videopost, id: {videopost.id}, título: {videopost.title}")
        return redirect(url_for('core.dashboard_MC'))

    return render_template('create_videopost.html', form=form)


@posts.route('/blog', methods=['GET', 'POST'])
def preview():

    return render_template('post.html')



@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)


    return render_template('post.html', post=post)


@posts.route('/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):

    post = Post.query.get_or_404(post_id)

    if current_user.is_authenticated:
        form = RegularPostForm()

        if form.validate_on_submit():

            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.photo_url = form.photo_url.data
            post.date_posted = datetime.now()
            post.content = form.content.data
            post.status =  form.status.data

            db.session.commit()
            flash(f"Editaste post id: {post.id}, título: {post.title}")

            return redirect(url_for('core.dashboard_MC'))

        elif request.method == 'GET':

            form.title.data = post.title
            form.subtitle.data = post.subtitle
            form.photo_url.data = post.photo_url
            form.content.data = post.content
            form.status.data = post.status

        return render_template('create_post.html', post=post, form=form)

    else:
        abort(403)

@posts.route('/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Blog_posts.query.get_or_404(post_id)

    if current_user.is_authenticated:
        flash(f"Eliminaste post: {post.id}, con título {post.title}")
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for("blog_posts.admin"))

#video

@posts.route('/<int:post_id>/update_videoblog', methods=['GET', 'POST'])
@login_required
def update_post_videoblog(post_id):

    videopost = Videopost.query.get_or_404(post_id)

    if current_user.is_authenticated:
        form = VideoPostForm()

        if form.validate_on_submit():

            videopost.title = form.title.data
            videopost.subtitle = form.subtitle.data
            videopost.photo_url = form.photo_url.data
            videopost.date_posted = datetime.now()
            videopost.content = form.content.data
            videopost.status =  form.status.data

            db.session.commit()
            flash(f"Editaste videopost id: {videopost.id}, título: {videopost.title}")

            return redirect(url_for('core.dashboard_MC'))

        elif request.method == 'GET':

            form.title.data = videopost.title
            form.subtitle.data = videopost.subtitle
            form.photo_url.data = videopost.photo_url
            form.content.data = videopost.content
            form.status.data = videopost.status

        return render_template('create_post.html', videopost=videopost, form=form)

    else:
        abort(403)


@posts.route('/<int:post_id>/delete_videoblog', methods=['GET', 'POST'])
@login_required
def delete_post_videoblog(post_id):
    videopost = Videopost.query.get_or_404(post_id)

    if current_user.is_authenticated:
        flash(f"Eliminaste post: {videopost.id}, con título {videopost.title}")
        db.session.delete(videopost)
        db.session.commit()
    return redirect(url_for("blog_posts.admin"))
