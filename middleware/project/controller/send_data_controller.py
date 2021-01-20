from project import app
from flask import render_template, request, jsonify
from time import sleep


{% for environment_device in environments_devices %}
@app.route("/{{environment_device[0]}}", methods=["POST"])
def environment_{{environment_device[0]}}():
    pass
{% endfor %}
