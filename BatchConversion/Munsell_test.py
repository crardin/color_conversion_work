import unittest
from BatchConversion.Munsell import Munsell


class TestMunsell(unittest.TestCase):
    def setUp(self):
        self.myMunsell = Munsell(5.1, 'PB', 4.6, 9.1)

    def test_H1_setting(self):
        self.myMunsell.H1 = 10
        self.assertEqual(10, self.myMunsell.H1)

    def test_H2_setting(self):
        self.myMunsell.H2 = 'RP'
        self.assertEqual('RP', self.myMunsell.H2)

    def test_V_setting(self):
        self.myMunsell.V = 1
        self.assertEqual(1, self.myMunsell.V)

    def test_C_setting(self):
        self.myMunsell.C = 2
        self.assertEqual(2, self.myMunsell.C)

    def test_MunsellValue(self):
        self.assertEqual('5.1PB 4.6/9.1', self.myMunsell.MunsellValue)

    def test_MunsellVector(self):
        self.assertListEqual(self.myMunsell.MunsellVector, [5.1, 'PB', 4.6, 9.1])

    def test_nominal_munsell(self):
        self.assertListEqual(self.myMunsell.NominalMunsellVector, [5, 'PB', 5, 9])

    def test_decimalHue(self):
        self.assertEqual(self.myMunsell.DecimalHue, 75.1)

    def test_nominalDecimalHue(self):
        self.assertEqual(self.myMunsell.NominalDecimalHue, 75)

    def test_findVerbalForValue(self):
        self.assertEqual("dark", self.myMunsell.findVerbalForValue(3))
        self.assertEqual("light", self.myMunsell.findVerbalForValue(7))
        self.assertEqual("middle", self.myMunsell.findVerbalForValue(4))

    def test_findVerbalForChroma(self):
        self.assertEqual("very weak", self.myMunsell.findVerbalForChroma(1))
        self.assertEqual("moderate", self.myMunsell.findVerbalForChroma(6))


if __name__ == "__main__":
    unittest.main()

