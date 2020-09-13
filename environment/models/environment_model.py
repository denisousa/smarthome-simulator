
from run import db
from datetime import datetime


class EnvironmentDB(db.Document):
    meta = {'collection': 'environment'}

    name = db.StringField(max_length=50, required=True)
    temperature = db.FloatField(required=True)
    noise = db.BooleanField(required=True)
    light = db.BooleanField(required=True)
