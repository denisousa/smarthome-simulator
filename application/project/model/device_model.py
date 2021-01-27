from project import db
from datetime import datetime


class {{device_class}}Status(db.EmbeddedDocument):
    name = db.StringField(max_length=50, unique=True, required=False)
    connect = db.BooleanField(required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)


class {{device_class}}Environment(db.EmbeddedDocument):
    {% for sensor in device["device"]["sensors"] %}
    {% if sensor == 'temperature' %}
    {{sensor}} = db.FloatField(required=False)
    {% endif %}
    {% if sensor == 'noise' %}
    {{sensor}} = db.BooleanField(required=False)
    {% endif %}
    {% if sensor == 'light' %}
    {{sensor}} = db.BooleanField(required=False)
    {% endif %}
    {% if sensor == 'motion' %}
    {{sensor}} = db.BooleanField(required=False)
    {% endif %}
    {% endfor %}
    data_from = db.StringField(max_length=50, required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)


class {{device_class}}DB(db.Document):
    meta = {'collection': '{{device_name}}'}
    environment = db.EmbeddedDocumentField({{device_class}}Environment, required=False)
