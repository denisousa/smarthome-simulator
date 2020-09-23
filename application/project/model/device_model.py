from project import db
from datetime import datetime


class {{device_class}}Device(db.EmbeddedDocument):
    temperature = db.FloatField(required=False)
    noise = db.BooleanField(required=False)
    light = db.BooleanField(required=False)
    data_from = db.StringField(max_length=50, required=False)
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
    {% endfor %}
    data_from = db.StringField(max_length=50, required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)


class {{device_class}}DB(db.Document):
    meta = {'collection': '{{name_device}}'}
    device = db.EmbeddedDocumentField({{device_class}}Device, required=False)
    environment = db.EmbeddedDocumentField({{device_class}}Environment, required=False)
