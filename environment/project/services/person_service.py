from project.entitys.person_entity import Person
from project.models.person_model import PersonDB


def find_person_by_name(name: str):
    return PersonDB.objects(name=name).first()


def find_person_by_id(id: str):
    return PersonDB.objects.get(id=id)


def create_person(name: str):
    person = {'name': name}
    PersonDB(**person).save()
