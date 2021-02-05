from project import app, socketio
from flask import render_template
import requests
from project.util.components_config import (
    people_config,
    devices_config,
    environments_config
)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           people_config=people_config,
                           devices_config=devices_config,
                           environments_config=environments_config)


@app.route("/middleware", methods=["GET"])
def middleware():
    devices = requests.get('http://localhost:5002/get_all_devices_name').json()
    devices_data = []
    for device in devices:
        data = requests.get(f'http://localhost:5002/get_all_by_device_name/{device}').json()
        devices_data.append((device, data))
    
    commands_sent = requests.get(f'http://localhost:5002/get_all_commands_sent').json()
    return render_template("middleware.html",
                            devices_data=devices_data,
                            commands_sent=commands_sent)


@app.route("/log", methods=["GET"])
def log():
    return render_template("log.html")