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
    return {"name_device": name for name in yaml_config["devices"]}


def get_descriptions_devices_list(yaml_config):
    return [description for description in yaml_config["devices"]["Description"]]


def get_names_var(yaml_config, type_config):
    names_var = []
    for config in yaml_config:
        name = config[type_config]["name"]
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
    t = Template(base_config).render(**{obj: yaml_config[header_yaml]})
    print(t)
    with open(path, "w") as f:
        f.write(t)
    print("\n\n")

def get_environment_devices(yaml_config, environments):
    new_complete = []
    for environment in environments:
        new = []
        for device in yaml_config["devices"]:
            if environment == device["device"]["environment"].lower().replace(" ", "_"):
                new.append(
                    unidecode(device["device"]["name"].lower().replace(" ", "_"))
                )
        new_complete.append((environment, new))
    return new_complete


generate_new_project()


devices_config = get_yaml_config("devices_config.yaml")
names_devices = get_names_var(devices_config["devices"], "device")
environments_config = get_yaml_config("environments_config.yaml")
names_environments = get_names_var(environments_config["environments"], "environment")
names_environments = {name: name for name in names_environments}
environments_devices = get_environment_devices(devices_config, names_environments)

for name_device, device in zip(names_devices, devices_config["devices"]):
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

for name_device, device in zip(names_devices, devices_config["devices"]):
    communications = [unidecode(communication.lower().replace(" ", "_")) for communication in device['device']['communications']]
    r = open(
        f"../new_application/project/communication/publisher/device_publisher.py", "r"
    ).read()
    f = open(
        f"../new_application/project/communication/publisher/{name_device}_publisher.py", "w"
    )
    t = Template(r).render(name_device=name_device, communications=communications)
    f.write(t)
    f.close()

for name in names_devices:
    r = open(
        f"../new_application/project/communication/subscriber/device_subscriber.py", "r"
    ).read()
    f = open(
        f"../new_application/project/communication/subscriber/{name}_subscriber.py", "w"
    )
    t = Template(r).render(name_device=name)
    f.write(t)
    f.close()

for device in names_devices:
    r = open(f"../new_application/project/static/js/device.js", "r").read()
    f = open(f"../new_application/project/static/js/{device}.js", "w")
    t = Template(r).render(device=device)
    f.write(t)
    f.close()

components_config = open("../application/project/util/components_config.py", "r").read()
environment_controller = open("../environment/project/controller/environment_controller.py", "r").read()
main_controller = open("../application/project/controller/main_controller.py", "r").read()
init_py = open("../application/project/__init__.py", "r").read()
main_js = open("../application/project/static/js/main.js", "r").read()
start_subscribers = open("../application/project/util/start_subscribers.py", "r").read()

t = Template(environment_controller).render(**{"environments": names_environments})
with open("../new_environment/project/controller/environment_controller.py", "w") as f:
    f.write(t)

t = Template(components_config).render(**{"devices_config": devices_config["devices"],"environments_config": environments_config["environments"],})
with open("../new_application/project/util/components_config.py", "w") as f:
    f.write(t)

t = Template(main_controller).render(**{"environments_devices": environments_devices, "devices": names_devices})
with open("../new_application/project/controller/main_controller.py", "w") as f:
    f.write(t)

t = Template(init_py).render(**{"devices": names_devices})
with open("../new_application/project/__init__.py", "w") as f:
    f.write(t)

t = Template(main_js).render(**{"environments": names_environments})
with open("../new_application/project/static/js/main.js", "w") as f:
    f.write(t)

t = Template(environment_controller).render(**{"environments": names_environments})
with open("../new_environment/project/controller/environment_controller.py", "w") as f:
    f.write(t)

t = Template(start_subscribers).render(**{"devices": names_devices})
with open("../new_application/project/util/start_subscribers.py", "w") as f:
    f.write(t)

os.remove("../new_application/project/model/device_model.py")
os.remove("../new_application/project/service/device_service.py")
os.remove("../new_application/project/communication/publisher/device_publisher.py")
os.remove("../new_application/project/communication/subscriber/device_subscriber.py")
os.remove("../new_application/project/static/js/device.js")
"""
    base_config = open(path_construct_scenario, "r").read()
    devices_config = Template(base_config).render(yaml_config=yaml_config['devices'])
    print(devices_config)
    with open(path_construct_scenario, "w") as f:
        f.write(devices_config)
"""

"""
    {% for device in devices %}
    {% if environment == device["device"]["environment"] %}
    {{device}}_service.save_data_environment(data)
    {% endif %}
    {% endfor %}
"""
