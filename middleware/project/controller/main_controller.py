from project import app
from flask import render_template, request, jsonify
from project.util.components_config import people_config, devices_config, environments_config
from project.service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
from time import sleep
from project import socketio


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           people_config=people_config,
                           devices_config=devices_config,
                           environments_config=environments_config)

{% for environment_device in environments_devices %}
@app.route("/{{environment_device[0]}}", methods=["POST"])
def environment_{{environment_device[0]}}():
    pass
{% endfor %}
