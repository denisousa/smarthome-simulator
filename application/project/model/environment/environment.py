class Environment:
    def __init__(self):
        __temperature: float = self.temperature # temperatura
        __proximity: bool = self.proximity # presença
        __noise: bool = self.noise # barulho
        __location: (float,float) = self.location # latitude e longitude
        __light: bool = self.light # iluminado
    
    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @property
    def proximity(self):
        return self.__proximity

    @proximity.setter
    def proximity(self, proximity):
        self.__proximity = proximity

    @property
    def noise(self):
        return self.__noise

    @noise.setter
    def noise(self, noise):
        self.__noise = noise

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def light(self):
        return self.__light

    @light.setter
    def light(self, light):
        self.__light = light
