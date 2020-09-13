import random


class Environment(object):
    def __init__(self):
        self.temperature: float = round(random.uniform(28, 30), 2)
        self.noise: bool = random.choices([True, False], [0.5, 0.5], k=1)[0]
        self.light: bool = random.choices([True, False], [0.5, 0.5], k=1)[0]

    @property
    def __dict__(self):
        return {
            "temperature": self.temperature,
            "noise": self.noise,
            "light": self.light,
        }

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @property
    def noise(self):
        return self.__noise

    @noise.setter
    def noise(self, noise):
        self.__noise = noise

    @property
    def light(self):
        return self.__light

    @light.setter
    def light(self, light):
        self.__light = light
