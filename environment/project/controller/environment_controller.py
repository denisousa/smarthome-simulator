from project import app
from flask import Flask, jsonify
from project.services.environment_service import (
    create_environment,
    find_environment_by_name,
    clean_environment,
    insert_person_environment,
    empity_environments,
    update_proximty,
)
from project.services.person_service import (
    create_person
)
from project.util.components_config import (
    people,
    environments,
    people_names,
    env_names,
    env_qtd,
    new_env_probality,
)
from datetime import datetime
import requests
import json
from time import sleep
import random


@app.route("/")
def main():
    {% for environment in environments %}
    try:
        create_environment("{{ environment }}")
    except:
        pass{% endfor %}
    {% for person in people %}
    try:
        create_person("{{ person['person']['name'].lower() }}")
    except:
        pass{% endfor %} 

    while True:
        empity_environments()
        for name in people_names:
            env_choice = random.choices(env_names, k=1)[0]
            insert_person_environment(name.lower(), env_choice)
        
        for name in env_names:
            update_proximty(name)

        {% for environment in environments %}
        environment, people = clean_environment(find_environment_by_name("{{environment}}"))
        environment = json.loads(environment.to_json())
        environment['data_from'] = '{{environment}}'
        if people:
            environment['people'] = people
        requests.post('http://localhost:5000/{{ environment }}', json=environment)
        {% endfor %}
        sleep(5)
    return jsonify({'msg': 'Success send :)'}), 200
