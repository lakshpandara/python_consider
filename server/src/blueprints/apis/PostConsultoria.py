import requests

from flask import Blueprint, render_template, redirect, url_for, session, request
from flask_restful import Resource, abort, reqparse

import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore
from os.path import join, dirname, realpath

UPLOADS_PATH = join(dirname(realpath(__file__)), 'considerado-app-firebase-adminsdk-85gzw-99c77d0ec2.json')

cred = credentials.Certificate(UPLOADS_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()

api_pc = Blueprint('homepost', __name__, url_prefix='')

def abort_if_post_doesnt_exist(post_id):
    post_ref = db.collection('PostConsulta')
    ref = post_ref.where(u'postid', u'==', post_id)
    if not ref:
        abort(404, message="Task {} doesn't exist".format(post_id))

parser = reqparse.RequestParser()
parser.add_argument('_emailcriador', location='form')
parser.add_argument('_idcriador', location='form')
parser.add_argument('_fotocriador', location='form')
parser.add_argument('fconsultoria', location='form')
parser.add_argument('festado', location='form')
parser.add_argument('fcidade', location='form')
parser.add_argument('fnome', location='form')
parser.add_argument('fexperiencia', location='form')
parser.add_argument('fpreco', location='form')
parser.add_argument('ftempo', location='form')
parser.add_argument('fsemana', location='form', action='append')
parser.add_argument('fhinicial', location='form')
parser.add_argument('fhfinal', location='form')
parser.add_argument('fphone', location='form')
parser.add_argument('femail', location='form')

class PostConsulta(object):
    def __init__(self, _emailcriador, _idcriador, _fotocriador, fconsultoria, festado, fcidade, fnome, fexperiencia, fpreco, ftempo, fsemana, fhinicial, fhfinal, fphone, femail):
        self._emailcriador = _emailcriador
        self._idcriador = _idcriador
        self._fotocriador = _fotocriador
        self.fconsultoria = fconsultoria
        self.festado = festado
        self.fcidade = fcidade
        self.fnome = fnome
        self.fexperiencia = fexperiencia
        self.fpreco = fpreco
        self.ftempo = ftempo
        self.fsemana = fsemana
        self.fhinicial = fhinicial
        self.fhfinal = fhfinal
        self.fphone = fphone
        self.femail = femail

    def to_dict(self):
        post = {
            '_emailcriador': self._emailcriador,
            '_idcriador': self._idcriador,
            '_fotocriador': self._fotocriador,
            'fconsultoria': self.fconsultoria,
            'festado': self.festado,
            'fcidade': self.fcidade,
            'fnome': self.fnome,
            'fexperiencia': self.fexperiencia,
            'fpreco': self.fpreco,
            'ftempo': self.ftempo,
            'fsemana': self.fsemana,
            'fhinicial': self.fhinicial,
            'fhfinal': self.fhfinal,
            'fphone': self.fphone,
            'femail': self.femail
        }
        return post

    def __repr__(self):
        return 'PostConsulta(_emailcriador={}, _idcriador={}, _fotocriador={}, fconsultoria={}, festado={}, fcidade={}, fnome={}, fexperiencia={}, fpreco={}, ftempo={}, fsemana={}, fhinicial={}, fhfinal={}, fphone={}, femail={})'.format(self._emailcriador, self._idcriador, self._fotocriador, self.fconsultoria, self.festado, self.fcidade, self.fnome, self.fexperiencia, self.fpreco, self.ftempo, self.fsemana, self.fhinicial, self.fhfinal, self.fphone, self.femail)

class PostConsultaList(Resource):
    def get(self):
        posts_ref = db.collection('PostConsulta')
        docs = posts_ref.stream()
        posts = {}
        for doc in docs:
            posts[doc.id]= doc.to_dict()
        return posts

    def post(self):
        args = parser.parse_args()
        post = PostConsulta(_emailcriador=args['_emailcriador'], _idcriador=args['_idcriador'], _fotocriador=args['_fotocriador'], fconsultoria=args['fconsultoria'], festado=args['festado'], fcidade=args['fcidade'], fnome=args['fnome'], fexperiencia=args['fexperiencia'], fpreco=args['fpreco'], ftempo=args['ftempo'], fsemana=args['fsemana'], fhinicial=args['fhinicial'], fhfinal=args['fhfinal'], fphone=args['fphone'], femail=args['femail'])
        db.collection('PostConsulta').add(post.to_dict())
        return post.to_dict(), 201

class PostConsultaListById(Resource):
    def get(self, postid):
        doc_ref = db.collection('PostConsulta').document(postid)
        if doc_ref:
            return doc_ref.get().to_dict()
        return None

    def put(self, postid):
        args = parser.parse_args()
        posts_ref = db.collection('PostConsulta')
        posts_ref.document(postid).update({"_emailcriador": args['_emailcriador'], "_idcriador": args['_idcriador'], "_fotocriador": args['_fotocriador'],"fconsultoria": args['fconsultoria'], "festado": args['festado'], "fcidade": args['fcidade'], "fnome": args['fnome'], "fexperiencia": args['fexperiencia'], "fpreco": args['fpreco'], "ftempo": args['ftempo'], "fsemana": args['fsemana'], "fhinicial": args['fhinicial'], "fhfinal": args['fhfinal'], "fphone": args['fphone'], "femail": args['femail']})
        return True, 201

    def delete(self, postid):
        posts_ref = db.collection('PostConsulta')
        posts_ref.document(postid).delete()
        return True, 201

class PostConsultaListByEmail(Resource):
    def get(self, postemail):
        doc_ref = db.collection('PostConsulta')
        query_ref = doc_ref.where(u'_emailcriador', u'==', postemail)
        docs = query_ref.stream()
        dicio = {}
        for doc in docs:
            dicio[doc.id] = doc.to_dict()
        if dicio:
            return dicio
        return None

class PostConsultaListByStateCity(Resource):
    def get(self, state, city):
        doc_ref = db.collection('PostConsulta')
        query_ref = doc_ref.where(u'festado', u'==', state).where(u'fcidade', u'==', city)
        docs = query_ref.stream()
        dicio = {}
        for doc in docs:
            dicio[doc.id] = doc.to_dict()
        if dicio:
            return dicio
        return None

class PostConsultaListByStateCitySearch(Resource):
    def get(self, state, city, search):
        doc_ref = db.collection('PostConsulta')
        query_ref = doc_ref.where(u'festado', u'==', state).where(u'fcidade', u'==', city).where(u'fconsultoria', u'==', search)
        docs = query_ref.stream()
        dicio = {}
        for doc in docs:
            dicio[doc.id] = doc.to_dict()
        if dicio:
            return dicio
        return None

@api_pc.route('/homesearch/', methods=['GET'])
def homesearch():
    if 'profile' in session:
        cc_estado = request.cookies.get('cookie_estado')
        cc_cidade = request.cookies.get('cookie_cidade')
        if request.method == "GET":
            pesquisa = request.form['fspesquisa'].replace(" ", "_")
            #https://app.considerado.org/
            dict_feed = requests.get('https://app.considerado.org/api/v1/search/'+ cc_estado +'/'+ cc_cidade +'/'+ pesquisa +'').json()
        return redirect(url_for('home.home', select_user = session['profile']['given_name'].replace(" ", ""), select_estado = cc_estado, select_cidade = cc_cidade))
    else:
        print("No username found in session HOMEPOST")
        return redirect(url_for('index.login', alert_index='index'))

@api_pc.route('/homepost/', methods=['POST'])
def homepost():
    if 'profile' in session:
        if request.method == "POST":
            req = request.form.to_dict(flat=False)
            req['_emailcriador'] = [session['profile']['email']]
            req['_idcriador'] = [session['profile']['id']]
            req['_fotocriador'] = [session['profile']['picture']]
            consultoria_alterada = req['fconsultoria'][0].replace(" ", "_")
            estado_alterado = req['festado'][0].replace(" ", "_")
            cidade_alterado = req['fcidade'][0].replace(" ", "_")
            req['fconsultoria'] = [consultoria_alterada]
            req['festado'] = [estado_alterado]
            req['fcidade'] = [cidade_alterado]
            #https://app.considerado.org/
            requests.post('https://app.considerado.org/api/v1/', data = req)
        cc_estado = request.cookies.get('cookie_estado')
        cc_cidade = request.cookies.get('cookie_cidade')
        return redirect(url_for('home.home', select_user = session['profile']['given_name'].replace(" ", ""), select_estado = cc_estado, select_cidade = cc_cidade))
    else:
        print("No username found in session HOMEPOST")
        return redirect(url_for('index.login', alert_index='index'))

@api_pc.route('/homedel/', methods=['POST'])
def homedel():
    if 'profile' in session:
        if request.method == "POST":
            req_id = request.form['fdmprofile']
            #https://app.considerado.org/
            requests.delete('https://app.considerado.org/api/v1/id/'+ req_id)
        cc_estado = request.cookies.get('cookie_estado')
        cc_cidade = request.cookies.get('cookie_cidade')
        return redirect(url_for('home.home', select_user = session['profile']['given_name'].replace(" ", ""), select_estado = cc_estado, select_cidade = cc_cidade))
    else:
        print("No username found in session HOMEDEL")
        return redirect(url_for('index.login', alert_index='index'))