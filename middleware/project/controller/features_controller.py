from project import app
from flask import render_template, request, jsonify
from project.service.middleware_service import (
    save_data,
    check_and_apply_strategies,
    get_all_data,
    get_all_data_by_device_name,
    pages,
)


@app.route("/get_pages", methods=["GET"])
def get_pages():
    data_page = pages()
    return jsonify(data_page), 200


@app.route("/get_all", methods=["GET"])
def get_all():
    return jsonify(get_all_data()), 200


@app.route("/get_all_by_device_name/<device_name>", methods=["GET"])
def get_all_by_device_name(device_name):
    return jsonify(get_all_data_by_device_name(device_name)), 200

