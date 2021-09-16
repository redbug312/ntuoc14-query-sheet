from flask import Blueprint, request, render_template, redirect, url_for, current_app

from ..models import Auth


lookup = Blueprint('lookup', __name__)


@lookup.route('/lookup')
def index():
    code = request.args.get('code')
    if code is None:
        return redirect(url_for('index'))
    return redirect(url_for('lookup.result', code=code), code=301)


@lookup.route('/lookup/<string:code>')
def result(code):
    query = Auth.query.filter_by(code=code).order_by(Auth.created_time.desc())
    auths = [{'badges': auth.get_badges(),
              'digits': auth.phone[-3:],
              'expired': auth.expired_after()}
             for auth in query.all() if not auth.is_expired()]
    auths += current_app.config['AUTHS']
    return render_template('lookup.pug', title=code, auths=auths)
