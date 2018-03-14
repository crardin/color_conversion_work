import unittest
from BatchConversion.Chroma import Chroma


class testChroma(unittest.TestCase):
    def setUp(self):
        self.myChroma = Chroma(6.2)

    def test_chroma_value(self):
        self.assertEqual(6.2, self.myChroma.C)

    def test_nominal_value(self):
        self.assertEqual(6, self.myChroma.NominalC)

    def test_nominal_value_zero(self):
        self.myChroma.C = 0.5
        self.assertEqual(0, self.myChroma.NominalC)

    def test_nominal_value_1(self):
        self.myChroma.C = 1.2
        self.assertEqual(1, self.myChroma.NominalC)

    def test_nominal_value_less_than_1(self):
        self.myChroma.C = 0.8
        self.assertEqual(1, self.myChroma.NominalC)


if __name__ == "__main__":
    unittest.main()

