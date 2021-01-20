from project import db
from project.models.person_model import PersonDB

class EnvironmentDB(db.Document):
    meta = {'collection': 'environment'}

    name = db.StringField(max_length=50, unique=True, required=True)
    temperature = db.FloatField(required=True)
    noise = db.BooleanField(required=True)
    light = db.BooleanField(required=True)
    motion = db.BooleanField(required=False)
    people = db.ListField(db.ReferenceField(PersonDB))
