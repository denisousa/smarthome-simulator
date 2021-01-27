from project import app, socketio
from flask import request, jsonify
from project.util.components_config import devices_config
from time import sleep
import requests

{% for device in device_actuator %}
@app.route('/{{device.split("|")[0]}}/actuator/{{device.split("|")[1]}}', methods=["POST"])
def {{device.split("|")[0]}}_{{device.split("|")[1]}}():
    requests.post("http://localhost:5001/escritorio/update", json=request.json)
    # socketio.emit("{{device.split("|")[0]}}_adapt", request.json)
    return jsonify({"msg": "updating environment"})
{% endfor %}