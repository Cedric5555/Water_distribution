from models.water_sources.water_source import WaterSource


class Well(WaterSource):
    """
    Represents underground water source.
    """

    def __init__(self, name: str, capacity: float, depth: float):
        super().__init__(name, capacity)
        self._depth = depth

    @property
    def depth(self):
        return self._depth

    def produce_water(self) -> float:
        # deeper wells produce less water
        production = self._capacity / self._depth
        return min(production, self._capacity)

    def cost_per_m3(self) -> float:
        return 0.10

    def __str__(self):
        return (
            f"Well: {self._name}, "
            f"Depth: {self._depth}m, "
            f"Capacity: {self._capacity}m3"
        )