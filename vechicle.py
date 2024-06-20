from abc import ABC, abstractmethod
class Vechicle(ABC):
    def __init__(self, name, model):
        print("vec")
        self.__name = name
        self.__model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass