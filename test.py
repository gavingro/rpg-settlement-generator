import unittest
from random import seed
from settlement import Settlement
from village import Village


class TestSettlement(unittest.TestCase):
    def setUp(self):
        seed(69)
        self.test_settlement = Settlement()

    def test_settlement_template(self):
        self.assertEqual(
            self.test_settlement.generate_template(),
            "This is the base settlement generator.",
        )
        self.assertEqual(
            self.test_settlement.template, "This is the base settlement generator.",
        )

    def test_settlement_attributes(self):
        self.assertIsNone(self.test_settlement.generate_attributes())

    def test_settlement_fill(self):
        self.assertNotIn(
            "{", self.test_settlement.fill_template(self.test_settlement.template)
        )

    def test_settlement_generator(self):
        self.assertIsInstance(self.test_settlement.generate(), str)
        print(self.test_settlement.generate())


class TestVillage(unittest.TestCase):
    def setUp(self):
        seed(69)
        self.test_village = Village()

    def test_village_attributes(self):
        self.assertIsInstance(self.test_village.name, str)
        self.assertIsInstance(self.test_village.water, str)
        self.assertIsInstance(self.test_village.resource, str)
        self.assertIsInstance(self.test_village.culture, str)
        self.assertIsInstance(self.test_village.noble_house, str)


if __name__ == "__main__":
    unittest.main()
