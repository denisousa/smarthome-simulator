import random


class Environment(object):
    def __init__(self, name):
        self.name: str = name
        self.temperature: float = round(random.uniform(28, 30), 2)
        self.noise: bool = random.choices([True, False], [0.5, 0.5], k=1)[0]
        self.light: bool = random.choices([True, False], [0.5, 0.5], k=1)[0]

    @property
    def __dict__(self):
        return {
            "name": self.name
            "temperature": self.temperature,
            "noise": self.noise,
            "light": self.light,
        }

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def temperature(self):
        return self.temperature

    @temperature.setter
    def temperature(self, temperature):
        self.temperature = temperature

    @property
    def noise(self):
        return self.noise

    @noise.setter
    def noise(self, noise):
        self.noise = noise

    @property
    def light(self):
        return self.light

    @light.setter
    def light(self, light):
        self.light = light
