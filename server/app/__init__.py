from flask import Flask, render_template, request, make_response, redirect, url_for, current_app, flash
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
from datetime import datetime, date, time
import random

from .models import Person, User, db
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
    name = request.values.get('name') or ''
    return render_template('query.pug', title='query', name=name)


@app.route('/reply', methods=['POST'])
def reply():
    name = request.form.get('name')
    people = Person.query.filter_by(name=name).all()
    if not people:
        flash(name, 'error')
        return redirect(url_for('query', name=name))
    else:
        for person in people:
            db.session.expunge(person)
            person.receipt = (person.receipt and
                              person.receipt.replace(" ", "").zfill(14))
        return render_template('reply.pug', title='reply', people=people)


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
    with app.app_context():
        db.create_all()
