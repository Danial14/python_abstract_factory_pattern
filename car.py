from land_vechicle import LandVechicle
class Car(LandVechicle):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.__name = name
        self.__model = model