import unittest
from BatchConversion.Munsell import Munsell


class TestMunsell(unittest.TestCase):
    def setUp(self):
        self.myMunsell = Munsell()

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

    def test_full_MunsellValue(self):
        self.myMunsell.H1 = 10
        self.myMunsell.H2 = 'RP'
        self.myMunsell.V = 1
        self.myMunsell.C = 2
        self.assertEqual('10RP 1/2', self.myMunsell.fullMunsellValue)


if __name__ == "__main__":
    unittest.main()

