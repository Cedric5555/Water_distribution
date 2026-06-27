from models.water_sources.water_source import WaterSource
from models.consumers.consumer import Consumer
from models.treatments.water_treatment import WaterTreatment


class WaterNetwork:
    """
    Controls the entire water distribution system.

    Stores sources, consumers and treatments.
    Uses polymorphism to interact with different objects.
    """

    def __init__(self):
        self._sources = []
        self._consumers = []
        self._treatments = []


    def add_source(self, source: WaterSource):
        """
        Add a water source to the network.
        """
        self._sources.append(source)


    def add_consumer(self, consumer: Consumer):
        """
        Add a consumer to the network.
        """
        self._consumers.append(consumer)


    def add_treatment(self, treatment: WaterTreatment):
        """
        Add a treatment method.
        """
        self._treatments.append(treatment)


    def total_production(self):
        """
        Calculate total produced water.

        Polymorphism happens here:
        Every source uses its own produce_water().
        """
        total = 0

        for source in self._sources:
            total += source.produce_water()

        return total


    def total_consumption(self):
        """
        Calculate total water consumption.

        Each consumer has different consumption.
        """
        total = 0

        for consumer in self._consumers:
            total += consumer.consume_water()

        return total


    def apply_treatment(self, amount):
        """
        Pass water through all treatment systems.
        """

        treated_amount = amount

        for treatment in self._treatments:
            treated_amount = treatment.purify(treated_amount)

        return treated_amount


    def treatment_cost(self):
        """
        Calculate total treatment cost.
        """

        total = 0

        for treatment in self._treatments:
            total += treatment.cost()

        return total


    def water_balance(self):
        """
        Check if there is enough water.
        """

        production = self.total_production()
        consumption = self.total_consumption()

        return production - consumption


    def generate_report(self):

        produced = self.total_production()
        consumed = self.total_consumption()
        remaining = self.water_balance()

        return (
            "\n===== WATER NETWORK REPORT =====\n"
            f"Total production: {produced} m3\n"
            f"Total consumption: {consumed} m3\n"
            f"Remaining water: {remaining} m3\n"
            f"Treatment cost: {self.treatment_cost()} PLN\n"
        )