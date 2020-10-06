from project import db


class PersonDB(db.Document):
    meta = {'collection': 'person'}
    name = db.StringField(max_length=50, unique=True, required=True)
