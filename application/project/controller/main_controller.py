from project import app
from flask import render_template, request, jsonify
'''from project.controller.{{device_controller}} import (
    {{device_connect}},
    {{device_disconnect}},
)'''
from project.util.connection_broker import Connection
from project.util.devices_config import devices_config
from project.util.environments_config import environments_config

from time import sleep
from project import socketio


@app.route("/", methods=["GET"])
def index():
    #start_controllers()
    return render_template("index.html",
                           devices_config=devices_config,
                           environments_config=environments_config)

{% for environment in environments %}
@app.route("/{{environment}}", methods=["POST"])
def environment_{{environment}}():
    body = request.json
    socketio.emit("{{environment}}", body)
    print(body)
    return jsonify({"msg": "Receive data"}), 200

{% endfor %}




'''@socketio.on("restart")
def restart():
    {{device_disconnect}}()
    connection = Connection()
    connection.channel.queue_delete(queue={{queue_device}})
    sleep(1)'''

'''
def start_controllers():
    {{device_connect}}
    {{device_disconnect}}'''

