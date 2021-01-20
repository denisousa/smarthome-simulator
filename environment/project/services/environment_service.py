from project.entitys.environment_entity import Environment
from project.models.environment_model import EnvironmentDB
from project.services.person_service import find_person_by_name
from project.util.components_config import env_names
import json


def clean_environment(environment):
    del environment.id
    del environment.name
    if environment.people:
        people = [f' {person.name.capitalize()}' for person in environment.people]
        return environment, people
    del environment.people
    return environment, []

def empity_environments():
    try:
        for name in env_names:
            EnvironmentDB.objects.get(name=name).update(people=None)
    except Exception:
        pass


def find_environment_by_name(name):
    return EnvironmentDB.objects(name=name).first()


def create_environment(name):
    environment = Environment(name).__dict__
    EnvironmentDB(**environment).save()

def insert_person_environment(person: str, environment: str):
    env = find_environment_by_name(environment)
    person_id = find_person_by_name(person).to_dbref()
    env.people.append(person_id)
    EnvironmentDB.objects.get(name=environment).update(people=env.people)

def update_proximty(name):
    env = EnvironmentDB.objects.get(name=name)
    if env.people:
        env.update(motion=True)
    else:
        env.update(motion=False)

def update_specific_data(environment_name: str, field, value):
    data = {f"set__{field}": value}
    EnvironmentDB.objects(name=environment_name).update(**data)
