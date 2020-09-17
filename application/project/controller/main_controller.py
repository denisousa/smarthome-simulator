from project import app
from flask import render_template, request, jsonify
'''from project.controller.{{device_controller}} import (
    {{device_connect}},
    {{device_disconnect}},
)'''
#from project.util.connection_broker import Connection
from project.util.components_config import devices_config, environments_config
from project.service import (
    {% for device in devices %}
    {{device}}_service,{% endfor %}
)
from project.communication.publisher import (
    {% for device in devices %}
    {{device}}_publisher,{% endfor %}
)
from time import sleep
from project import socketio


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           devices_config=devices_config,
                           environments_config=environments_config)

{% for environment_device in environments_devices %}
@app.route("/{{environment_device[0]}}", methods=["POST"])
def environment_{{environment_device[0]}}():
    data = request.json
    socketio.emit("{{environment_device[0]}}", data)
    {% for device in environment_device[1] %}
    data_clean = {{device.replace(' ', '_')}}_service.remove_fields(dict(data))
    {{device.replace(' ', '_')}}_service.save_data_environment(data_clean)
    {{device.replace(' ', '_')}}_publisher.{{device.replace(' ', '_')}}Publisher().start()
    socketio.emit("{{device.replace(' ', '_')}}", data_clean)
    {% endfor %}
    return jsonify({"msg": "Receive data"}), 200

{% endfor %}
