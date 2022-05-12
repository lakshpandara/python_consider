import os
import requests
from flask import Blueprint, current_app, render_template, redirect, url_for, session, make_response
from authlib.integrations.flask_client import OAuth
from flask_dance.contrib.google import make_google_blueprint, google

blueprint = make_google_blueprint()
bp_index = Blueprint('index', __name__, url_prefix='')

oauth = OAuth(current_app)
oauth.register(
    name='google',
    client_id='737136290734-c5pns0q9tq4vodmam21j9ve0pm3cur99.apps.googleusercontent.com',
    client_secret='owN7ia95jpre2a3fMPThFDQa',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

@bp_index.route('/')
@bp_index.route('/<string:alert_index>')
def index(alert_index = None):
    if 'profile' in session:
        return redirect(url_for('home.welcome', user_session = session['profile']['given_name'].replace(" ", "")))
    else:
        print("No username found in session INDEX")
        return render_template('layout/index.html')

@bp_index.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('index.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@bp_index.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = oauth.google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = oauth.google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    session['profile'] = user_info
    session['info_token'] = token
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect(url_for('home.welcome', user_session = session['profile']['given_name'].replace(" ", "")))

@bp_index.route('/logout')
def logout():
    if session['info_token']['access_token']:
        token = session['info_token']['access_token']
        resp = google.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
    for key in list(session.keys()):
        session.pop(key, None)
    return redirect(url_for('index.index', alert_index='index'))

@bp_index.errorhandler(404)
def page_not_found(error):
    return 'OPS!!, Isso foi um ERRO', 404