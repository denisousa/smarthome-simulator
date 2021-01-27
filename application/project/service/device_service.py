from project.model.{{device}}_model import {{device_class}}DB, {{device_class}}Environment
import contextlib


def remove_fields(data):
    # o problema ta aqui
    field_device_db = {{device_class}}Environment.__dict__['_reverse_db_field_map']
    try:
        del field_device_db['_id']
        del field_device_db['people']
    except:
        pass
    for field in list(data):
        if field not in list(field_device_db):
            del data[field]
    return data


def save_data_environment(data):
    {{device_class}}DB(environment=data).save()


def get_connection_status():
    status = {{device_class}}Status.objects(name="{{device_class}}").find()
    return status.connect


def connect_middleware():
    already_connected = {{device_class}}Status.objects(name="{{device_class}}").find()
    if already_connected:
        {{device_class}}Status.objects(name="{{device_class}}").update(set__connect=True)
    else:
        {{device_class}}Status(name="{{device_class}}", connect=True)


def disconnect_middleware(data):
    {{device_class}}Status(name="{{device_class}}", connect=False)

