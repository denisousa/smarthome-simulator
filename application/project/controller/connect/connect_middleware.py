from project import app
from flask import render_template, request, jsonify
from project.util.components_config import people_config, devices_config, environments_config
from project.service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
from time import sleep
from project import socketio
import requests
import json


@app.route("/connect_{{device_name}}", methods=["GET"])
def connect_{{device_name}}():
    {{device_name}}_service.connect_middleware()
    return jsonify({"msg": "Success connect"}), 200
