from project.model.middleware_model import MiddlewareDB
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


def get_state_device(device_name):
    all_data = MiddlewareDB.objects(data_from=device_name).to_json()
    return json.loads(all_data)[-1]


def parse_data(data):
    return {
        "temperature": data.temperature,
        "noise": data.noise,
        "light": data.light,
        "motion": data.motion,
        "environment": data.environment,
        "data_from": data.data_from,
    }