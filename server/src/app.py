import os
import uuid
  
from flask import Flask
from flask_restful import Api
from datetime import timedelta

#inport extension
from flask_sslify import SSLify

#inport plugins
from .blueprints.views.pwa import bp_pwa
from .blueprints.views.index import bp_index, blueprint
from .blueprints.views.home import bp_home
from .blueprints.views.about import bp_about
from .blueprints.views.term import bp_term
from .blueprints.apis.PostConsultoria import api_pc, PostConsultaListById, PostConsultaList, PostConsultaListByEmail, PostConsultaListByStateCity, PostConsultaListByStateCitySearch

app = Flask(__name__, instance_relative_config=True, static_url_path='')
api = Api(app)
app.secret_key = str(uuid.uuid4())

#init_app in extension
sslify = SSLify(app)

#Add api of Resources
api.add_resource(PostConsultaList, '/api/v1/')
api.add_resource(PostConsultaListById, '/api/v1/id/<postid>')
api.add_resource(PostConsultaListByEmail, '/api/v1/email/<postemail>')
api.add_resource(PostConsultaListByStateCity, '/api/v1/city/<state>/<city>')
api.add_resource(PostConsultaListByStateCitySearch, '/api/v1/search/<state>/<city>/<search>')

#register plugins
app.register_blueprint(blueprint, url_prefix="/login")
app.register_blueprint(bp_pwa)
app.register_blueprint(bp_index, url_prefix='/')
app.register_blueprint(bp_home)
app.register_blueprint(bp_about)
app.register_blueprint(bp_term)
app.register_blueprint(api_pc)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# set FLASK_APP=server/src/app.py
# set FLASK_ENV=development
# gcloud builds submit --tag gcr.io/considerado-app/considerado-1
# gcloud run deploy --image gcr.io/considerado-app/considerado-1