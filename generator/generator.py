import yaml
import os
from jinja2 import Template
from unidecode import unidecode
from datetime import datetime


def generate_new_project():
    os.system("rm -r ../new_application")
    os.system("rm -r ../new_environment")
    os.system("rm -r ../new_middleware")
    os.system("cp -r ../application ../new_application")
    os.system("cp -r ../environment ../new_environment")
    os.system("cp -r ../middleware ../new_middleware")
    os.system("cp -r ./images ../new_application/project/static/images")


def get_names_devices_list(yaml_config):
    return [name for name in yaml_config["devices"]]


def get_names_devices_dict(yaml_config):
    return {"device_name": name for name in yaml_config["devices"]}


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


def validate(device_name, actuator):
    return f"{device_name.replace(' ', '_').lower()}|{list(actuator.keys())[0]}"


def get_device_actuators(yaml_config):
    device_by_actuators = []
    for device in yaml_config["devices"]:
        if "actuators" in device["device"]:
            device_actuator = [
                validate(device["device"]["name"], actuator)
                for actuator in device["device"]["actuators"]
            ]
            device_by_actuators.append(
                device_actuator
            )
    return device_by_actuators


def configure_name(name):
    return name.lower().replace(" ", "_")


def get_value_actuator_by_device_name(devices_config, device, actuator):
    for device_config in devices_config:
        if device == configure_name(device_config["device"]["name"]):
            actuators = device_config["device"].get("actuators")
            if actuators:
                for act in actuators:
                    act_check = act.get(actuator)
                    if act_check:
                        return act_check


def get_environmnt_by_device_name(devices_config, device):
    for device_config in devices_config:
        if device == configure_name(device_config["device"]["name"]):
            return device_config["device"]["environment"].lower()

def parseStrBool(string):
    if string == "True":
        return True
    return False

def parser_DSL_Python(device, text):
    text = text.replace("when", "")
    text = replace_time(text)
    conditions, actions = text.split(" then ")
    actuator = get_actuator_name(actions)
    propertie = get_value_actuator_by_device_name(
        devices_config["devices"], device, actuator
    )
    env = get_environmnt_by_device_name(devices_config["devices"], device)
    action_value = actions.split("(")[1].replace(")", "")
    action_value = {propertie: parseStrBool(action_value), "environment": env}
    actions = f"requests.post('http://localhost:5000/{device}/actuator/{actuator}', json={action_value})"
    if "and" in conditions:
        conditions = conditions.split(" and ")
        new_format = []
        for condition in conditions:
            if "." in condition and "datetime" not in condition:
                device, sensor = condition.split(".")
                sensor, boolean = sensor.split(" is ")
                new_format.append(
                    f"get_state_by_device_name('{device[1:]}').get('{sensor}') is {boolean}"
                )
            else:
                new_format.append(condition)
        conditions = " and ".join(new_format)
        return f"if {conditions}:", actions
    else:
        return f"if{conditions}:", actions


def replace_time(text):
    text = text.replace("hour", "datetime.now().hour")
    text = text.replace("minute", "datetime.now().minute")
    text = text.replace("second", "datetime.now().second")
    text = text.replace("day", "datetime.now().day")
    return text


def get_actuator_name(actions):
    return actions.replace("(True)", "").replace("(False)", "")


generate_new_project()


devices_config = get_yaml_config("devices_config.yaml")
names_devices = get_names_var(devices_config["devices"], "device")
device_actuators = get_device_actuators(devices_config)
middleware_config = get_yaml_config("middleware_config.yaml")

environments_config = get_yaml_config("environments_config.yaml")
names_environments = get_names_var(environments_config["environments"], "environment")
names_environments = {name: name for name in names_environments}
environments_devices = get_environment_devices(devices_config, names_environments)

people_config = get_yaml_config("people_config.yaml")

for device_name, device in zip(names_devices, devices_config["devices"]):
    r = open(f"../new_application/project/model/device_model.py", "r").read()
    f = open(f"../new_application/project/model/{device_name}_model.py", "w")
    device_class = device_name.replace("_", " ").title().replace(" ", "")
    t = Template(r).render(
        device_name=device_name, device=device, device_class=device_class
    )
    f.write(t)
    f.close()

for name in names_devices:
    r = open(f"../new_application/project/service/device_service.py", "r").read()
    f = open(f"../new_application/project/service/{name}_service.py", "w")
    device_class = name.replace("_", " ").title().replace(" ", "")
    t = Template(r).render(device=name, device_class=device_class)
    f.write(t)
    f.close()

for device in names_devices:
    r = open(f"../new_application/project/static/js/device.js", "r").read()
    f = open(f"../new_application/project/static/js/{device}.js", "w")
    t = Template(r).render(device=device)
    f.write(t)
    f.close()


for device_actuator in device_actuators:
    r = open(
        f"../new_application/project/controller/actuator/actuator_controller.py", "r"
    ).read()
    f = open(
        f"../new_application/project/controller/actuator/{device_actuator[0].split('|')[0]}.py",
        "w",
    )
    env = get_environmnt_by_device_name(devices_config["devices"], device_actuator[0].split('|')[0])
    device_actuator = [f"{device_actuator[0]}|{env}"]
    t = Template(r).render(device_actuator=device_actuator)
    f.write(t)
    f.close()


for device_name in names_devices:
    r = open(f"../new_application/project/controller/connect/connect_middleware.py", "r").read()
    f = open(f"../new_application/project/controller/connect/{device_name}_connect.py", "w")
    t = Template(r).render(
        device_name=device_name,
    )
    f.write(t)
    f.close()


for device_name in names_devices:
    r = open(f"../new_application/project/controller/disconnect/disconnect_middleware.py", "r").read()
    f = open(f"../new_application/project/controller/disconnect/{device_name}.py", "w")
    t = Template(r).render(
        device_name=device_name,
    )
    f.write(t)
    f.close()

all_strategies = []
for devices_stategy in middleware_config["middleware"]:
    for strategy in devices_stategy["device"]["events"]:
        condition, action = parser_DSL_Python(devices_stategy["device"]["id"], strategy)
        all_strategies.append((condition, action))


components_config = open("../application/project/util/components_config.py", "r").read()
components_config_env = open(
    "../environment/project/util/components_config.py", "r"
).read()
environment_controller = open(
    "../environment/project/controller/environment_controller.py", "r"
).read()
update_controller = open(
    "../environment/project/controller/update_controller.py", "r"
).read()
receive_data = open(
    "../application/project/controller/receive_data/receive_data.py", "r"
).read()
middleware_receive_controller = open(
    "../middleware/project/controller/receive_data_controller.py", "r"
).read()
middleware_send_controller = open(
    "../middleware/project/controller/send_data_controller.py", "r"
).read()
middleware_service = open(
    "../middleware/project/service/middleware_service.py", "r"
).read()
init_py = open("../application/project/__init__.py", "r").read()
main_js = open("../application/project/static/js/main.js", "r").read()
# start_subscribers = open("../application/project/util/start_subscribers.py", "r").read()

t = Template(environment_controller).render(
    **{"environments": names_environments, "people": people_config["people"]}
)
with open("../new_environment/project/controller/environment_controller.py", "w") as f:
    f.write(t)

t = Template(update_controller).render(**{"environments": names_environments})
with open("../new_environment/project/controller/update_controller.py", "w") as f:
    f.write(t)

t = Template(components_config_env).render(
    **{"environments": names_environments, "people": people_config["people"]}
)
with open("../new_environment/project/util/components_config.py", "w") as f:
    f.write(t)

t = Template(components_config).render(
    **{
        "devices_config": devices_config["devices"],
        "environments_config": environments_config["environments"],
        "people_config": people_config["people"],
    }
)
with open("../new_application/project/util/components_config.py", "w") as f:
    f.write(t)

t = Template(receive_data).render(
    **{"environments_devices": environments_devices, "devices": names_devices}
)
with open("../new_application/project/controller/receive_data/receive_data.py", "w") as f:
    f.write(t)

t = Template(middleware_receive_controller).render(**{"names_devices": names_devices})
with open("../new_middleware/project/controller/receive_data_controller.py", "w") as f:
    f.write(t)

t = Template(middleware_send_controller).render(**{"names_devices": names_devices})
with open("../new_middleware/project/controller/send_data_controller.py", "w") as f:
    f.write(t)

t = Template(middleware_service).render(**{"strategies": all_strategies})
with open("../new_middleware/project/service/middleware_service.py", "w") as f:
    f.write(t)

t = Template(init_py).render(**{"devices": names_devices, "device_actuator": device_actuators})
with open("../new_application/project/__init__.py", "w") as f:
    f.write(t)

t = Template(main_js).render(**{"environments": names_environments})
with open("../new_application/project/static/js/main.js", "w") as f:
    f.write(t)

# t = Template(start_subscribers).render(**{"devices": names_devices})
# with open("../new_application/project/util/start_subscribers.py", "w") as f:
#     f.write(t)

os.remove("../new_application/project/model/device_model.py")
os.remove("../new_application/project/service/device_service.py")
os.remove("../new_application/project/controller/connect/connect_middleware.py")
os.remove("../new_application/project/controller/disconnect/disconnect_middleware.py")
os.remove("../new_application/project/controller/actuator/actuator_controller.py")
os.remove("../new_application/project/static/js/device.js")

