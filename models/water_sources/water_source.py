from abc import ABC, abstractmethod


class WaterSource(ABC):
    """
    Abstract base class representing a general water source.

    Every water source must:
    - have a name
    - have a water capacity
    - be able to produce water
    - have a production cost
    """

    def __init__(self, name: str, capacity: float):
        self._name = name
        self._capacity = capacity

    @property
    def name(self):
        return self._name

    @property
    def capacity(self):
        return self._capacity

    @abstractmethod
    def produce_water(self) -> float:
        """
        Returns the amount of water produced.
        Every subclass must implement this.
        """
        pass

    @abstractmethod
    def cost_per_m3(self) -> float:
        """
        Returns the cost of producing 1 cubic meter of water.
        """
        pass

    def __str__(self):
        return f"{self._name} (Capacity: {self._capacity} m3)"