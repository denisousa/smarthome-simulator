from project import app
from flask import render_template, request, jsonify
from project.service.middleware_service import (
    save_data,
    check_and_apply_strategies,
    get_all_data,
    get_all_data_by_device_name,
    get_state_by_device_name,
    check_device_has_been_disconnected,
    get_all_connected_devices,
    get_all_disconnected_devices,
    connect_device_by_device_name,
    disconnect_device_by_device_name,
)
from flasgger import swag_from


# @app.route("/get_pages", methods=["GET"])
# def get_pages():
#     data_page = pages()
#     return jsonify(data_page), 200


@swag_from(f"{app.config['DOCUMENTATION']}get_all.yaml")
@app.route("/get_all", methods=["GET"])
def get_all():
    return jsonify(get_all_data()), 200


@swag_from(f"{app.config['DOCUMENTATION']}get_all_by_device_name.yaml")
@app.route("/get_all_by_device_name/<device_name>", methods=["GET"])
def get_all_device_name(device_name):
    return jsonify(get_all_data_by_device_name(device_name)), 200


@swag_from(f"{app.config['DOCUMENTATION']}get_state_by_device_name.yaml")
@app.route("/get_state_by_device_name/<device_name>", methods=["GET"])
def get_state_device_name(device_name):
    return jsonify(get_state_by_device_name(device_name)), 200


@swag_from(f"{app.config['DOCUMENTATION']}check_device_has_been_disconnected.yaml")
@app.route("/check_device_has_been_disconnected/<device_name>", methods=["GET"])
def check_device_has_disconnected(device_name):
    device = check_device_has_been_disconnected(device_name)
    if device:
        return jsonify({"msg":"The device has not been disconnected", "result": False}), 200
    return jsonify({"msg":"The device has been disconnected", "result": True}), 200


@swag_from(f"{app.config['DOCUMENTATION']}get_all_connected_devices.yaml")
@app.route("/get_all_connected_devices", methods=["GET"])
def get_connected_devices():
    devices_connected = get_all_connected_devices()
    return jsonify(devices_connected), 200


@swag_from(f"{app.config['DOCUMENTATION']}get_all_disconnected_devices.yaml")
@app.route("/get_all_disconnected_devices", methods=["GET"])
def get_disconnected_devices():
    devices_disconnected = get_all_disconnected_devices()
    return jsonify(devices_disconnected), 200


@swag_from(f"{app.config['DOCUMENTATION']}connect_device_by_device_name.yaml")
@app.route("/connect_device_by_device_name/<device_name>", methods=["GET"])
def connect_device(device_name):
    msg, result = connect_device_by_device_name(device_name)
    return jsonify({"msg": msg, "result": result}), 200


@swag_from(f"{app.config['DOCUMENTATION']}disconnect_device_by_device_name.yaml")
@app.route("/disconnect_device_by_device_name/<device_name>", methods=["GET"])
def disconnect_device(device_name):
    msg, result = disconnect_device_by_device_name(device_name)
    return jsonify({"msg": msg, "result": result}), 200
