from flask import Flask, jsonify
from services import envrironment_service
from flask_mongoengine import MongoEngine
from datetime import datetime
import requests
from time import sleep


app = Flask(__name__)
app.config["MONGODB_HOST"] = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false'
db = MongoEngine(app)

@app.route("/")
def main():
    {% for environment in environments %}
    envrironment_service.create_environment({{ envrironment }}){% endfor %}


    {% for environment in environments %}
    requests.post('http://localhost:5000/{{ environment }}', json={{ environment }}.__dict__)
    {% endfor %}
    return jsonify({'msg': 'Success send :)'}), 200



if __name__ == "__main__":
    app.run(port=5001)
