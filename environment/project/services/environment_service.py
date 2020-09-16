from project.entitys.environment_entity import Environment
from project.models.environment_model import EnvironmentDB

def clean_environment(environment):
    del environment.id
    del environment.name
    return environment


def find_environment_by_name(name):
    environment = EnvironmentDB.objects(name=name).first()
    return clean_environment(environment)
    

def create_environment(name):
    environment = Environment(name).__dict__
    EnvironmentDB(**environment).save()

