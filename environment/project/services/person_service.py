from project.entitys.person_entity import Person
from project.models.person_model import PersonDB


def find_person_by_name(name: str):
    return PersonDB.objects(name=name).first()


def create_person(name: str):
    person = {'name': name}
    PersonDB(**person).save()
