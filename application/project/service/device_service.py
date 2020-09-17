from project.model.{{device}}_model import {{device}}DB


def remove_fields(data):
    field_device_db = {{device}}DB.__dict__['_reverse_db_field_map']
    print({{device}}DB().__dict__['_cls'])
    print(data)
    print(field_device_db)
    try:
        del field_device_db['_id']
    except:
        pass
    for field in list(data):
        if field not in list(field_device_db):
            del data[field]
    print(data)
    return data

def save_data_environment(data):
    data = remove_fields(dict(data))
    {{device}}DB(**data).save()

