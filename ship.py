from water_vechicle import WaterVechicle

class Ship(WaterVechicle):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.__name = name
        self.__model = model