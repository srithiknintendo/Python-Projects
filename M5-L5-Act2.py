from abc import ABC
from abc import abstractmethod
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        print("stopped")
class Car(Vehicle):
    def __init__(self, name):
        self.name = name
    def start(self):
        print("vroom vromm")
    def stop(self):
        print("stopped")
bmw = Car("bmw m5")
bmw.start()
bmw.stop()
