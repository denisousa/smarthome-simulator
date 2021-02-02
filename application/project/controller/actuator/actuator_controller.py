from project import app, socketio
from flask import request, jsonify
from project.util.components_config import devices_config
from project.service import (
    {% for device in device_actuator %}
    {{device.split("|")[0]}}_service,{% endfor %}
)
import requests
from time import sleep


{% for device in device_actuator %}
@app.route('/{{device.split("|")[0]}}/actuator/{{device.split("|")[1]}}', methods=["POST"])
def {{device.split("|")[0]}}_{{device.split("|")[1]}}():
    body = dict(request.json) 
    # Preciso atualizar os dados do dispositivo e do ambiente no simulador
    # socketio.emit("device", data_clean)
    state = {{device.split("|")[0]}}_service.get_state()
    del request.json["environment"]
    key, value = request.json.popitem()
    state[key] = value
    sleep(1)
    socketio.emit("{{device.split("|")[0]}}", state)
    res = requests.post("http://localhost:5001/{{device.split("|")[2]}}/update", json=body).json()
    print(f"res: {res}")
    socketio.emit("{{device.split("|")[2]}}", sort_dict(res))
    return jsonify({"msg": "updating environment"})
{% endfor %}



def sort_dict(data):
    return {
        "temperature": data["temperature"],
        "noise": data["noise"],
        "light": data["light"],
        "motion": data["motion"],
        "people": data["people"],
    }