import os
from flask import render_template, flash, redirect, request, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
from app import app, db
from app.forms import joinDirectory, mediums
from app.models import User
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'app\static'
configure_uploads(app, photos)
users = {}

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    title = 'Upload your photo'
    if request.method == 'POST' and 'photo' in request.files:
        user = User.query.order_by(User.id.desc()).first()
        file = request.files['photo']
        filename = photos.save(file, name="{}.jpg".format(user.id))
        return render_template('directory.html')
    return render_template(('upload.html'))

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('base.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/directory')
def directory():
    user = User.query.all()
    return render_template('directory.html', user=user)

@app.route('/directory/join', methods=['GET', 'POST'])
def join_directory():
    title = 'One of us!'
    form = joinDirectory()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
                    email=form.email.data, medium=form.medium.data)
        db.session.add(user)
        db.session.commit()
        user_id = User.query.order_by(User.id.desc()).first()
        users['user'] = user_id
        flash('Join request for {} {}'.format(
            form.first_name.data, form.last_name.data))
        return redirect('/upload')
    return render_template('join_directory.html', title=title, form=form, mediums=mediums)

@app.route('/about')
def about():
    return render_template('about.html')

