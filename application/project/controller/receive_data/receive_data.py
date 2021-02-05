from project import app
from flask import render_template, request, jsonify
from project.service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
from time import sleep
from project import socketio
import requests
import json
from datetime import datetime


{% for environment_device in environments_devices %}
@app.route("/{{environment_device[0]}}", methods=["POST"])
def environment_{{environment_device[0]}}():
    data = request.json
    print(f"data_clean: {data}")
    socketio.emit("{{environment_device[0]}}", data)
    {% for device in environment_device[1] %}
    data_clean = {{device.replace(' ', '_')}}_service.remove_fields(dict(data))

    socketio.emit("{{device.replace(' ', '_')}}", data_clean)

    {{device.replace(' ', '_')}}_service.save_data_environment(dict(data_clean))
    data_clean["environment"] = data_clean["data_from"]
    data_clean["data_from"] = "{{device.replace(' ', '_')}}"

    requests.post('http://localhost:5002/receive-data/{{device.replace(' ', '_')}}', json=data_clean)
    {% endfor %}
    return jsonify({"msg": "Receive data"}), 200

{% endfor %}