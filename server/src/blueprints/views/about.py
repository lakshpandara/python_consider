from flask import Blueprint, render_template, redirect


bp_about = Blueprint('about', __name__)

@bp_about.route('/about')
def about():
    return render_template('layout/about.html')