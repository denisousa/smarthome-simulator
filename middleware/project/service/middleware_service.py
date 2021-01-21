from project.model.middleware_model import MiddlewareDB, MiddlewareDisconnectedDevicesDB
from datetime import datetime
import math
import requests
import json


def check_and_apply_strategies():
    {% for strategy in strategies %}
    {{strategy[0]}}
        {{strategy[1]}}

    {% endfor %}


def save_data(data):
    MiddlewareDB(**data).save()

def pages(page):
    """The total number of pages"""
    # print(MiddlewareDB.objects.paginate(page=1, per_page=10))
    # print(MiddlewareDB.objects.paginate(page=1, per_page=10).items)
    all_data = MiddlewareDB.objects.paginate(page=1, per_page=10).items
    return [parse_data(data) for data in all_data]
    # print(data.data_from)
    # print(dir(MiddlewareDB.objects.paginate(page=1, per_page=10)))
    # return int(math.ceil(MiddlewareDB.total / float(MiddlewareDB.per_page)))

def get_all_data():
    return MiddlewareDB.objects.as_pymongo()


def get_all_data_by_device_name(device_name):
    return MiddlewareDB.objects(data_from=device_name).as_pymongo()


def get_state_by_device_name(device_name):
    all_data = MiddlewareDB.objects(data_from=device_name).to_json()
    return json.loads(all_data)[-1]


def check_device_has_been_disconnected(device_name):
    device = MiddlewareDB.objects(data_from=device_name).first()
    if device:
        return True
    return False


def get_all_connected_devices():
    devices = set()
    devices_disconnected = set()
    all_devices = MiddlewareDB.objects().as_pymongo()
    all_devices_disconnected = MiddlewareDisconnectedDevicesDB.objects().as_pymongo()
    [devices.add(device["data_from"]) for device in all_devices]
    [devices_disconnected.add(device["data_from"]) for device in all_devices_disconnected]
    return list(devices.difference(devices_disconnected))


def get_all_disconnected_devices():
    return MiddlewareDisconnectedDevicesDB.objects().as_pymongo()

def connect_device_by_device_name(device_name):
    device = MiddlewareDB.objects(name=device_name).first()
    if device:
        return  "The device is already connected", False
    MiddlewareDisconnectedDevicesDB.objects.get(name=device_name).delete()
    return "Success in connect the device", True

def disconnect_device_by_device_name(device_name):
    device_disconnected = MiddlewareDisconnectedDevicesDB.objects(name=device_name).first()
    if device_disconnected:
        return  "Device has already been disconnected", False
    environment = get_state_by_device_name(device_name)["environment"]
    device = {"name": device_name, "environment": environment}
    MiddlewareDisconnectedDevicesDB.save(**device)
    return "Success in removing the device", True


def parse_data(data):
    return {
        "temperature": data.temperature,
        "noise": data.noise,
        "light": data.light,
        "motion": data.motion,
        "environment": data.environment,
        "data_from": data.data_from,
    }