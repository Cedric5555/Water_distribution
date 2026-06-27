from models.water_sources.water_source import WaterSource


class Reservoir(WaterSource):
    """
    Represents stored water.
    """

    def __init__(
        self,
        name: str,
        capacity: float,
        stored_amount: float
    ):
        super().__init__(name, capacity)
        self._stored_amount = stored_amount


    @property
    def stored_amount(self):
        return self._stored_amount


    def produce_water(self) -> float:
        return min(
            self._stored_amount,
            self._capacity
        )


    def cost_per_m3(self) -> float:
        return 0.07


    def __str__(self):
        return (
            f"Reservoir: {self._name}, "
            f"Stored: {self._stored_amount}m3"
        )