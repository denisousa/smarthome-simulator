from ..entitys.environment import Environment
from ..models.environment_model import EnvironmentDB


def find_envrionment_by_name(name):
    return EnvironmentDB.objects(name=name).first()


def create_environment(name):
    environment = Environment(name).__dict__
    equipamento = EnvironmentDB(**environment).save()
    return str(equipamento.id)
