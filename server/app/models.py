from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column('ROWID', db.Integer, primary_key=True)
    name = db.Column('姓名', db.String(32), index=True, nullable=False)
    depart = db.Column('系所', db.String(32), nullable=False)
    obtain = db.Column('領取方式', db.String(32), nullable=False)
    zipcode = db.Column('郵遞區號', db.String(32))
    receipt = db.Column('郵局執據號碼', db.String(32))
    comment = db.Column('備註', db.String(32))
