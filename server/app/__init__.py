from flask import Flask, render_template, request, make_response, redirect, url_for, current_app, flash
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
from datetime import datetime, date, time
import random

from .models import User, db
from .views.api import users
from .views.signin import signin
from .views.signup import signup

app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.register_blueprint(users)
app.register_blueprint(signin)
app.register_blueprint(signup)
app.config.from_pyfile('instance/default.py')
app.config.from_pyfile('instance/development.py', silent=True)

migrate = Migrate(app, db)


@app.route('/')
def index():
    return redirect(url_for('query'))


@app.route('/query')
def query():
    return render_template('query.pug', title='query')


@app.route('/query/redirect', methods=['POST'])
def query_redirect():
    name = request.form.get('name')
    if name == 'foo':
        flash(name, 'error')
        return redirect(url_for('query'))
    else:
        return redirect(url_for('reply'))


@app.route('/reply')
def reply():
    return render_template('reply.pug', title='reply')


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
    with app.app_context():
        db.create_all()
