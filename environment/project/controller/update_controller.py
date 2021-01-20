from project import app
from flask import Flask, jsonify, request
from project.services.environment_service import (
    update_specific_data
)
import json

{% for environment in environments %}
@app.route("/{{ environment }}/update", methods=["POST"])
def {{environment}}_update():
    print("I'M ADAPT")
    env = request.json["environment"]
    del request.json["environment"]
    for key, value in request.json.items():
        update_specific_data(env, key, value)
    return jsonify({'msg': 'Success update :)'}), 200
{% endfor %}