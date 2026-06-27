import unittest

from models.water_sources.river import River
from models.water_sources.well import Well
from models.water_sources.reservoir import Reservoir


class TestWaterSources(unittest.TestCase):

    def test_river_production(self):
        river = River("River", 10000, 8000)

        self.assertEqual(
            river.produce_water(),
            8000
        )


    def test_well_production(self):
        well = Well("Well", 5000, 50)

        self.assertEqual(
            well.produce_water(),
            100
        )


    def test_reservoir_production(self):
        reservoir = Reservoir(
            "Reservoir",
            8000,
            6000
        )

        self.assertEqual(
            reservoir.produce_water(),
            6000
        )


if __name__ == "__main__":
    unittest.main()