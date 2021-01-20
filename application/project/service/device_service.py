from project.model.{{device}}_model import {{device_class}}DB, {{device_class}}Environment
import contextlib


def remove_fields(data):
    # o problema ta aqui
    field_device_db = {{device_class}}Environment.__dict__['_reverse_db_field_map']
    try:
        del field_device_db['_id']
    except:
        pass
    #_ = [del data[field] if field not in list(field_device_db) and field != 'data_from' for field in list(data)]
    for field in list(data):
        if field not in list(field_device_db):
            del data[field]
    return data

def save_data_environment(data):
    {{device_class}}DB(environment=data).save()

def save_data_device(data):
    {{device_class}}DB(device=data).save()
