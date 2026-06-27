from models.water_sources.water_source import WaterSource


class River(WaterSource):
    """
    Represents a river water source.

    A river has a high natural water production rate
    and a low production cost.
    """

    def __init__(self, name: str, capacity: float, flow_rate: float):
        super().__init__(name, capacity)
        self._flow_rate = flow_rate

    @property
    def flow_rate(self):
        return self._flow_rate

    def produce_water(self) -> float:
        """
        Calculates how much water the river can produce.
        """
        return min(self._flow_rate, self._capacity)

    def cost_per_m3(self) -> float:
        """
        Rivers are cheap water sources.
        """
        return 0.05

    def __str__(self):
        return (
            f"River: {self._name}, "
            f"Flow rate: {self._flow_rate} m3, "
            f"Capacity: {self._capacity} m3"
        )