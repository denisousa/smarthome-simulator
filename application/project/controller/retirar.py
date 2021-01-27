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


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           people_config=people_config,
                           devices_config=devices_config,
                           environments_config=environments_config)


@app.route("/middleware", methods=["GET"])
def middleware():
    devices = requests.get('http://localhost:5002/get_all_connected_devices').json()
    devices_data = []
    for device in devices:
        data = requests.get(f'http://localhost:5002/get_all_by_device_name/{device}').json()
        data = data[-50] if len(data) >= 50 else data
        devices_data.append((device, data))
    
    commands_sent = requests.get(f'http://localhost:5002/get_all_commands_sent').json()
    return render_template("middleware.html",
                            devices_data=devices_data,
                            commands_sent=commands_sent)


{% for device in environments_devices %}
@app.route("/connect_{{device}}", methods=["GET"])
def connect_{{device}}():
    {{device}}_service.connect_middleware()
    return jsonify({"msg": "Success connect"}), 200
{% endfor %}


{% for device in environments_devices[1] %}
@app.route("/disconnect_{{device}}", methods=["GET"])
def disconnect_{{device}}():
    {{device}}_service.disconnect_middleware()
    return jsonify({"msg": "Success disconnect"}), 200
{% endfor %}


{% for environment_device in environments_devices %}
@app.route("/{{environment_device[0]}}", methods=["POST"])
def environment_{{environment_device[0]}}():
    data = request.json
    socketio.emit("{{environment_device[0]}}", data)
    {% for device in environment_device[1] %}
    data_clean = {{device.replace(' ', '_')}}_service.remove_fields(dict(data))
    {{device.replace(' ', '_')}}_service.save_data_environment(dict(data_clean))
    data_clean["environment"] = data_clean["data_from"]
    data_clean["data_from"] = "{{device.replace(' ', '_')}}"
    requests.post('http://localhost:5002/receive-data/{{device.replace(' ', '_')}}', json=data_clean)
    socketio.emit("{{device.replace(' ', '_')}}", data_clean)
    {% endfor %}
    return jsonify({"msg": "Receive data"}), 200

{% endfor %}
