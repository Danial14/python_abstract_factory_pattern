from vechicle import Vechicle
class WaterVechicle(Vechicle):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.__name = name
        self.__model = model
    def start(self):
        print(f"{self.__name} started")
    def stop(self):
        print(f"{self.__model}")