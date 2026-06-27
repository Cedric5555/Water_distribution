from abc import ABC, abstractmethod


class WaterTreatment(ABC):

    def __init__(self, name):
        self._name = name


    @abstractmethod
    def purify(self, amount):
        pass


    @abstractmethod
    def cost(self):
        pass