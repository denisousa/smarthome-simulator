import yaml
import os
from jinja2 import Template
from unidecode import unidecode

def generate_new_project():
    os.system("rm -r ../new_application")
    os.system("rm -r ../new_environment")
    os.system("cp -r ../application ../new_application")
    os.system("cp -r ../environment ../new_environment")
    os.system("cp -r ./images ../new_application/project/static/images")


def get_names_devices_list(yaml_config):
    return [name for name in yaml_config["devices"]]


def get_names_devices_dict(yaml_config):
    return {'name_device': name for name in yaml_config["devices"]}


def get_descriptions_devices_list(yaml_config):
    return [description for description in yaml_config["devices"]['Description']]

def get_names_var(yaml_config, type_config):
    names_var = []
    for config in yaml_config:
        name = config[type_config]['name']
        names_var.append(unidecode(name).lower().replace(" ", "_"))
    return names_var

def get_yaml_config(path):
    with open(path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def apply_new_code(path, path_yaml, header_yaml, obj):
    with open(path_yaml) as f:
        yaml_config = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_config)

    base_config = open(path, "r").read()
    t = Template(base_config).render(**{obj:yaml_config[header_yaml]})
    print(t)
    with open(path, "w") as f:
        f.write(t)
    print('\n\n')


generate_new_project()

apply_new_code("../new_application/project/util/devices_config.py",
               "devices_config.yaml",
               "devices",
               "devices_config")

apply_new_code("../new_application/project/util/environments_config.py",
               "environments_config.yaml",
               "environments",
               "environments_config")


def get_environment_devices(yaml_config, environments):
    new_complete = []
    for environment in environments:
        new = []
        for device in yaml_config['devices']:
            if environment == device["device"]["environment"].lower().replace(" ", "_"):
                new.append(unidecode(device["device"]["name"].lower().replace(" ", "_")))
        new_complete.append((environment, new))
    return new_complete

devices_config = get_yaml_config('devices_config.yaml')
names_devices = get_names_var(devices_config['devices'], 'device')

environments_config = get_yaml_config('environments_config.yaml')
names_environments = get_names_var(environments_config['environments'], 'environment')

names_environments = {name:name for name in names_environments}

environments_devices = get_environment_devices(devices_config, names_environments)

environment_controller = open('../environment/project/controller/environment_controller.py', "r").read()
main_controller = open('../application/project/controller/main_controller.py', "r").read()
init_py = open('../application/project/__init__.py', "r").read()
main_js = open('../application/project/static/js/main.js', "r").read()

t = Template(environment_controller).render(**{'environments':names_environments})
with open('../new_environment/project/controller/environment_controller.py', "w") as f:
    f.write(t)

for name_device, device in zip(names_devices, devices_config['devices']):
    r = open(f"../new_application/project/model/device_model.py", "r").read()
    f = open(f"../new_application/project/model/{name_device}_model.py", "w")
    t = Template(r).render(name_device=name_device, device=device)
    f.write(t)
    f.close()

for name in names_devices:
    r = open(f"../new_application/project/service/device_service.py", "r").read()
    f = open(f"../new_application/project/service/{name}_service.py", "w")
    t = Template(r).render(device=name)
    f.write(t)
    f.close()

for environment in names_environments:
    r = open(f"../new_application/project/static/js/environment.js", "r").read()
    f = open(f"../new_application/project/static/js/{environment}.js", "w")
    t = Template(r).render(environment=environment)
    f.write(t)
    f.close()


'''for name in names_devices:
    open(f"../new_application/project/communication/publisher/{name}_publisher.py", "a").read()

for name in names_devices:
    open(f"../new_application/project/communication/subscriber/{name}_subscriber.py", "a").read()
'''

t = Template(main_controller).render(**{'environments_devices':environments_devices, 'devices':names_devices})
with open('../new_application/project/controller/main_controller.py', "w") as f:
    f.write(t)


t = Template(init_py).render(**{'devices':names_devices})
with open('../new_application/project/__init__.py', "w") as f:
    f.write(t)

t = Template(main_js).render(**{'environments':names_environments})
with open('../new_application/project/static/js/main.js', "w") as f:
    f.write(t)



os.remove("../new_application/project/model/device_model.py")
os.remove("../new_application/project/service/device_service.py")
'''
    base_config = open(path_construct_scenario, "r").read()
    devices_config = Template(base_config).render(yaml_config=yaml_config['devices'])
    print(devices_config)
    with open(path_construct_scenario, "w") as f:
        f.write(devices_config)
'''

'''
    {% for device in devices %}
    {% if environment == device["device"]["environment"] %}
    {{device}}_service.save_data_environment(data)
    {% endif %}
    {% endfor %}
'''