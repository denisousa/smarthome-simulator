from project import app
from flask import render_template, request, jsonify
from project.service.middleware_service import (
    save_data,
    check_and_apply_strategies
)


{% for name_device in names_devices %}
@app.route("/receive-data/{{name_device}}", methods=["POST"])
def receive_from_{{name_device}}():
    save_data(request.json)
    check_and_apply_strategies()
    return jsonify({"msg": "ok"}), 200
{% endfor %}
