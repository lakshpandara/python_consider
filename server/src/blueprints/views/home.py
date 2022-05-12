import requests

from flask import Blueprint, render_template, redirect, session, url_for, request, make_response

bp_home = Blueprint('home', __name__, url_prefix='')

@bp_home.route('/welcome/<string:user_session>/', methods=['GET','POST'])
def welcome(user_session):
    if 'profile' in session:
        if request.method == "POST":
            estado = request.form['fwestado'].replace(" ", "_")
            cidade = request.form['fwcidade'].replace(" ", "_")
            return redirect(url_for('home.home', select_user = session['profile']['given_name'].replace(" ", ""), select_estado = estado, select_cidade = cidade))
        return render_template('layout/welcome.html', user = session['profile']['given_name'].replace(" ", ""))
    else:
        print("No username found in session WELCOME")
        return redirect(url_for('index.login', alert_index='index'))

@bp_home.route('/home/<string:select_estado>/<string:select_cidade>/<string:select_user>/', methods=['GET','POST'])
def home(select_estado, select_cidade, select_user):
    if 'profile' in session:
        dict_user = {
            "_id" : session['profile']['id'],
            "_namefull" : session['profile']['name'],
            "_name" : session['profile']['given_name'],
            "_email" : session['profile']['email'],
            "_photho" : session['profile']['picture']
        }
        if request.method == "POST":
            cc_estado = request.cookies.get('cookie_estado')
            cc_cidade = request.cookies.get('cookie_cidade')
            pesquisa = request.form['fspesquisa'].replace(" ", "_")
            #https://app.considerado.org/
            dict_posts = requests.get('https://app.considerado.org/api/v1/email/'+ session['profile']['email']).json()
            dict_feed = requests.get('https://app.considerado.org/api/v1/search/'+ cc_estado +'/'+ cc_cidade +'/'+ pesquisa +'').json()
            return render_template('layout/home.html', dict_user = dict_user, dict_posts = dict_posts, dict_feed = dict_feed)
        #https://app.considerado.org
        dict_posts = requests.get('https://app.considerado.org/api/v1/email/'+ session['profile']['email']).json()
        dict_feed = requests.get('https://app.considerado.org/api/v1/city/'+ select_estado +'/'+ select_cidade +'').json()

        response = make_response(render_template('layout/home.html', dict_user = dict_user, dict_posts = dict_posts, dict_feed = dict_feed))
        response.set_cookie('cookie_estado', select_estado)
        response.set_cookie('cookie_cidade', select_cidade)
        return response
    else:
        print("No username found in session HOME")
        return redirect(url_for('index.login', alert_index='index'))


