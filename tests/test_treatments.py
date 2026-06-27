import unittest

from models.treatments.sand_filter import SandFilter
from models.treatments.uv_treatment import UVTreatment


class TestTreatments(unittest.TestCase):

    def test_sand_filter(self):

        filter = SandFilter("Filter")

        self.assertEqual(
            filter.purify(1000),
            950
        )


    def test_uv_treatment(self):

        uv = UVTreatment("UV")

        self.assertEqual(
            uv.purify(1000),
            980
        )


if __name__ == "__main__":
    unittest.main()