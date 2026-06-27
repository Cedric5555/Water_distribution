import unittest

from models.consumers.house import House
from models.consumers.farm import Farm
from models.consumers.factory import Factory


class TestConsumers(unittest.TestCase):

    def test_house_consumption(self):
        house = House("House")

        self.assertEqual(
            house.consume_water(),
            300
        )


    def test_farm_consumption(self):
        farm = Farm("Farm")

        self.assertEqual(
            farm.consume_water(),
            2000
        )


    def test_factory_consumption(self):
        factory = Factory("Factory")

        self.assertEqual(
            factory.consume_water(),
            5000
        )


if __name__ == "__main__":
    unittest.main()