from project import db
from datetime import datetime


class {{name_device}}DB(db.Document):
    meta = {'collection': '{{name_device}}'}
    {% for sensor in device["device"]["sensors"] %}
    {% if sensor == 'temperature' %}
    {{sensor}} = db.FloatField(required=True)
    {% endif %}
    {% if sensor == 'noise' %}
    {{sensor}} = db.BooleanField(required=True)
    {% endif %}
    {% if sensor == 'light' %}
    {{sensor}} = db.BooleanField(required=True)
    {% endif %}
    {% endfor %}

