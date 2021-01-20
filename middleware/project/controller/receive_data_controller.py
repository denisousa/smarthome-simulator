from project import app
from flask import render_template, request, jsonify
from project.service.middleware_service import (
    save_data,
    check_and_apply_strategies
)

call_once = True

{% for name_device in names_devices %}
@app.route("/receive-data/{{name_device}}", methods=["POST"])
def receive_from_{{name_device}}():
    global call_once
    save_data(request.json)
    success = check_and_apply_strategies()
    if success:
        call_once = False
    return jsonify({"msg": "ok"}), 200
{% endfor %}
