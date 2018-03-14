import unittest
from BatchConversion.H2 import H2


class TestH2(unittest.TestCase):
    def setUp(self):
        self.myH2 = H2('Y')

    def test_H2_value(self):
        self.assertEqual('Y', self.myH2.H2)

    def test_getHueLetterCode(self):
        angle = 90
        H2Value = self.myH2.getHueLetterCode(angle)
        self.assertEqual('Y', H2Value)

    def test_getNominalValue(self):
        self.assertEqual('Y', self.myH2.NominalH2)

    def test_getNumericValue(self):
        self.assertEqual(20, self.myH2.NumericH2)


if __name__ == "__main__":
    unittest.main()
