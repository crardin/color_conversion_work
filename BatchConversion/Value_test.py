import unittest
from BatchConversion.Value import Value


class testValue(unittest.TestCase):
    def setUp(self):
        self.myValue = Value(1.7)

    def test_Value_value(self):
        self.assertEqual(1.7, self.myValue.V)

    def test_nominal_value(self):
        self.assertEqual(2, self.myValue.NominalV)

    def test_negative_value(self):
        self.myValue.V = -5
        self.assertEqual(1, self.myValue.NominalV)


if __name__ == "__main__":
    unittest.main()
