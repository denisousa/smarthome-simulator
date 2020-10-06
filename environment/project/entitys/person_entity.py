class Person(object):
    def __init__(self, name, environment):
        self.name: str = name

    @property
    def __dict__(self):
        return {
            "name": self.name
        }
