from flask import Blueprint, render_template, redirect


bp_term = Blueprint('term', __name__)

@bp_term.route('/term')
def term():
    return render_template('layout/term.html')