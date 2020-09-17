from project.model.{{device}}_model import {{device}}DB


def remove_fields(data):
    field_device_db = {{device}}DB.__dict__['_reverse_db_field_map']
    try:
        del field_device_db['_id']
    except:
        pass
    for field in list(data):
        if field not in list(field_device_db):
            del data[field]
    return data

def save_data_environment(data):
    {{device}}DB(**data).save()

