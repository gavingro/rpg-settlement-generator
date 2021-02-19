import unittest
from random import seed
from settlement import Settlement


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


if __name__ == "__main__":
    unittest.main()
