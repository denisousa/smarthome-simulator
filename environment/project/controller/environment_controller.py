from project import app
from flask import Flask, jsonify
from project.services import environment_service
from datetime import datetime
import requests
import json
from time import sleep


@app.route("/")
def main():
    {% for environment in environments %}
    try:
        environment_service.create_environment("{{ environment }}")
    except:
        pass
    {% endfor %}
    while True:
        {% for environment in environments %}
        environment = json.loads(environment_service.find_environment_by_name("{{environment}}").to_json())
        environment['data_from'] = '{{environment}}'
        requests.post('http://localhost:5000/{{ environment }}', json=environment)
        {% endfor %}
        sleep(5)
    return jsonify({'msg': 'Success send :)'}), 200
