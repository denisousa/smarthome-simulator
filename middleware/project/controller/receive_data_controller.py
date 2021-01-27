from project import app
from flask import render_template, request, jsonify
from project.service.middleware_service import (
    save_data,
    check_and_apply_strategies,
    check_device_has_been_disconnected,
)
from datetime import datetime

current_minute = datetime.now().minute

{% for name_device in names_devices %}
@app.route("/receive-data/{{name_device}}", methods=["POST"])
def receive_from_{{name_device}}():
    global current_minute
    result = check_device_has_been_disconnected(request.json["data_from"])
    if not result:
        save_data(request.json)
        if current_minute != datetime.now().minute:
            check_and_apply_strategies()
            current_minute = datetime.now().minute
    return jsonify({"msg": "ok"}), 200
{% endfor %}
