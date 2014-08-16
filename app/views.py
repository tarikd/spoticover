from app import app, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from spoticover import SpotifyScavenger, CoversCollage



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # if g.user is not None and g.user.is_authenticated():
    # 	return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
    	session['remember_me'] = form.remember_me.data
    	login = form.login.data
    	password = form.password.data
    	scavenger = SpotifyScavenger(login, password)
    	toplist = scavenger.get_user_toplist()
    	scavenger.save_covers(toplist)
    	cover = CoversCollage(img_folder, 'facebook_cover')
    	cover.make_picture()
    	return render_template('download.html')
    return render_template('login.html',
        title = 'Sign In',
        form = form)

@app.route('/download')
def download(login, password):
	file = "faceboo_cover.jpg"
	response = make_response(file)
	response.headers["Content-Disposition"] = "attachment; filename=facebook_cover.jpg"
	with open("facebook_cover.jpg", 'r') as f:
		body = f.read()
	return make_response((body, headers))


@lm.user_loader
def load_user(userid):
    return User.get(userid)







