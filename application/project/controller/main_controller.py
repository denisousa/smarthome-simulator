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


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           people_config=people_config,
                           devices_config=devices_config,
                           environments_config=environments_config)

@app.route("/middleware", methods=["GET"])
def middleware():
    return render_template("middleware.html")

{% for environment_device in environments_devices %}
@app.route("/{{environment_device[0]}}", methods=["POST"])
def environment_{{environment_device[0]}}():
    data = request.json
    socketio.emit("{{environment_device[0]}}", data)
    {% for device in environment_device[1] %}
    data_clean = {{device.replace(' ', '_')}}_service.remove_fields(dict(data))
    # TODO: Alterar o clean para eu não fazer as linhas 28 e 29
    data_clean["environment"] = data_clean["data_from"]
    data_clean["data_from"] = "{{device.replace(' ', '_')}}" 
    requests.post('http://localhost:5002/receive-data/{{device.replace(' ', '_')}}', json=data_clean)
    socketio.emit("{{device.replace(' ', '_')}}", data_clean)
    {% endfor %}
    return jsonify({"msg": "Receive data"}), 200

{% endfor %}
