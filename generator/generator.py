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
        names_var.append(unidecode(name).lower())
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

environments_config = get_yaml_config('environments_config.yaml')
names_environments = get_names_var(environments_config['environments'],
                                   'environment')

names_environments = {name:name for name in names_environments}

base_config = open('../environment/run.py', "r").read()
main_controller = open('../application/project/controller/main_controller.py', "r").read()
main_js = open('../application/project/static/js/main.js', "r").read()
#import ipdb; ipdb.set_trace()
t = Template(base_config).render(**{'environments':names_environments})
with open('../new_environment/run.py', "w") as f:
    f.write(t)

t = Template(main_controller).render(**{'environments':names_environments})
with open('../new_application/project/controller/main_controller.py', "w") as f:
    f.write(t)

t = Template(main_js).render(**{'environments':names_environments})
with open('../new_application/project/static/js/main.js', "w") as f:
    f.write(t)


'''
    base_config = open(path_construct_scenario, "r").read()
    devices_config = Template(base_config).render(yaml_config=yaml_config['devices'])
    print(devices_config)
    with open(path_construct_scenario, "w") as f:
        f.write(devices_config)
'''