import os
from flask import (
    Blueprint, make_response, send_from_directory
)

bp_pwa = Blueprint('pwa', __name__, url_prefix='')


@bp_pwa.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')


@bp_pwa.route('/sw.js')
def service_worker():
    response = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response