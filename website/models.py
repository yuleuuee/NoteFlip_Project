# this is where we create our database models

from . import db  # means: from __init__ .py import db object
from flask_login import UserMixin
# from sqlalchemy.sql import func
from datetime import datetime

#******************************************************************** Table for USERS ***********************************************************#
#  table for users
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


#******************************************************************** Table for NOTES ***********************************************************#

# table for notes
class Note(db.Model):
     id = db.Column(db.Integer, primary_key =True)
     data = db.Column(db.String(5000))
     date = db.Column(db.DateTime,default = datetime.now()) # datetime.now()| datetime.utcnow()
     user_id = db.Column(db.Integer,db.ForeignKey('user.id')) # 1:n --> one to many relation

     


 