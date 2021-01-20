from project import db
from datetime import datetime


class MiddlewareDB(db.Document):
    meta = {'collection': 'middleware'}
    temperature = db.FloatField(required=False)
    noise = db.BooleanField(required=False)
    light = db.BooleanField(required=False)
    motion = db.BooleanField(required=False)
    data_from = db.StringField(max_length=50, required=False)
    environment = db.StringField(max_length=50, required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)