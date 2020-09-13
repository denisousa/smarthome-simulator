from flask import Flask, jsonify
from environment import Environment
from datetime import datetime
import requests
from time import sleep

app = Flask(__name__)


@app.route("/")
def main():
    {% for environment in environments %}
    {{ environment }} = Environment(){% endfor %}


    date = datetime.now()
    while True:
        {% for environment in environments %}
        requests.post('http://localhost:5000/{{ environment }}', json={{ environment }}.__dict__)
        {% endfor %}
        return jsonify({'msg': 'Success send :)'}), 200
        #sleep(1)


if __name__ == "__main__":
    app.run(port=5001)
