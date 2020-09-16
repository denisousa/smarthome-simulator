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
    {% for environment in environments %}
    environment = environment_service.find_environment_by_name("{{environment}}").to_json()
    requests.post('http://localhost:5000/{{ environment }}', json=json.loads(environment))
    sleep(5)
    {% endfor %}
    return jsonify({'msg': 'Success send :)'}), 200
