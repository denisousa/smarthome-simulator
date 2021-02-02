from project import app
from flask import Flask, jsonify, request
from project.services.environment_service import (
    update_specific_data,
    find_environment_by_name
)
from project.services.person_service import (
    find_person_by_id
)
import json

{% for environment in environments %}
@app.route("/{{ environment }}/update", methods=["POST"])
def {{environment}}_update():
    env = request.json["environment"]
    del request.json["environment"]
    for key, value in request.json.items():
        update_specific_data(env, key, value)
    env = json.loads(find_environment_by_name("{{environment}}").to_json())
    del env["name"]
    del env["_id"]
    env["people"] = [find_person_by_id(person["$oid"]).name.capitalize() for person in env["people"]]
    return jsonify(env), 200
{% endfor %}
