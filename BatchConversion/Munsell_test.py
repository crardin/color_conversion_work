import unittest
from Munsell import Munsell


class TestMunsell(unittest.TestCase):
    def setUp(self):
        self.myMunsell = Munsell(5.1, 'PB', 4.6, 9.1)

    def test_H1_setting(self):
        self.myMunsell.H1 = 10
        self.assertEqual(10, self.myMunsell.H1)

    def test_H1_setting_pound(self):
        self.myMunsell.H1 = '#'
        self.assertEqual('#', self.myMunsell.H1)

    def test_H1_setting_non_number(self):
        pass
        # self.MyMunsell.H1 = 'A'
        # self.assertRaises()

    def test_H1_setting_outside_range(self):
        pass

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

    def find_nominal_munsell(self, value):
        # should take a list representing a munsell value
        self.myMunsell.H1 = value[0]
        self.myMunsell.H2 = value[1]
        self.myMunsell.V = value[2]
        self.myMunsell.C = value[3]

    def test_nominal_munsell(self):
        self.find_nominal_munsell([5.1, 'PB', 4.6, 9.1])
        self.assertListEqual(self.myMunsell.NominalMunsellVector, [5, 'PB', 5, 10])
        self.find_nominal_munsell([2.1, 'YR', 5, 7.5])
        self.assertListEqual(self.myMunsell.NominalMunsellVector, [2.5, 'YR', 5, 8])
        self.find_nominal_munsell([0.3, 'PB', 6.1, 3])
        self.assertListEqual(self.myMunsell.NominalMunsellVector, [10, 'B', 6, 4])
        self.find_nominal_munsell([0.1, 'YR', 5.7, 12.1])
        self.assertListEqual(self.myMunsell.NominalMunsellVector, [10, 'R', 6, 12])

    def test_decimalHue(self):
        self.assertEqual(self.myMunsell.DecimalHue, 75.1)

    def test_nominalDecimalHue(self):
        self.assertEqual(self.myMunsell.NominalDecimalHue, 75)

    def test_find_nominal_H1(self):
        self.find_nominal_H1(2.1)
        self.assertEqual(self.myMunsell.Nominal_H1, 2.5)

    def find_nominal_H1(self, H1):
        self.myMunsell.H1 = H1
        self.myMunsell.findNominalH1()

    def test_find_nominal_H1_for_1(self):
        self.find_nominal_H1(1)
        self.assertEqual(self.myMunsell.Nominal_H1, 10)

    def test_find_nominal_H1_for_less_than_1(self):
        self.find_nominal_H1(0.2)
        self.assertEqual(self.myMunsell.Nominal_H1, 10)

    def test_find_nominal_H1_high_value(self):
        self.find_nominal_H1(10)
        self.assertEqual(self.myMunsell.H1, 10)

    def test_find_nominal_H1_pound(self):
        self.find_nominal_H1('#')
        self.assertEqual(self.myMunsell.Nominal_H1, 'N')

    def find_nominal_v(self, value):
        self.myMunsell.V = value
        self.myMunsell.findNominalValue()

    def find_nominal_v_between_1_and_10(self):
        self.find_nominal_v(1)
        self.assertTrue(1 <= self.myMunsell.Nominal_V <= 10)
        self.find_nominal_v(4.4)
        self.assertTrue(1 <= self.myMunsell.Nominal_V <= 10)
        self.find_nominal_v(7.7)
        self.assertTrue(1 <= self.myMunsell.Nominal_V <= 10)

    def find_nominal_v_is_whole_number(self):
        self.find_nominal_v(1)
        self.assertTrue(self.myMunsell.Nominal_V.is_integer())
        self.find_nominal_v(4.4)
        self.assertTrue(self.myMunsell.Nominal_V.is_integer())
        self.find_nominal_v(7.7)
        self.assertTrue(self.myMunsell.Nominal_V.is_integer())

    def test_find_nominal_C(self):
        self.find_nominal_v(4.1)
        self.assertEqual(self.myMunsell.Nominal_V, 4)
        self.find_nominal_c(9.1)
        self.assertEqual(self.myMunsell.Nominal_C, 10)

    def find_nominal_c(self, value):
        self.myMunsell.C = value
        self.myMunsell.findNominalChroma()

    def test_find_nominal_C_low_value(self):
        # test for a chroma value less than 0.5
        self.find_nominal_c(0.3)
        self.assertEqual(self.myMunsell.Nominal_C, 0)

    def test_find_nominal_C_low_range(self):
        # test for a chroma value between 0.5 and 1.5
        self.find_nominal_c(0.7)
        self.assertEqual(self.myMunsell.Nominal_C, 1)
        self.find_nominal_c(1.5)
        self.assertEqual(self.myMunsell.Nominal_C, 1)
        self.find_nominal_c(0.5)
        self.assertEqual(self.myMunsell.Nominal_C, 1)

    def test_find_nominal_c_high_range(self):
        # test for a chroma value greater than 1.5
        self.find_nominal_c(1.6)
        self.assertEqual(self.myMunsell.Nominal_C, 2)
        self.find_nominal_c(11.9)
        self.assertEqual(self.myMunsell.Nominal_C, 12)
        self.find_nominal_c(15.2)
        self.assertEqual(self.myMunsell.Nominal_C, 16)

    def is_even(self, value):
        return value % 2 == 0

    def test_find_nominal_c_high_range_is_even(self):
        # test to make sure a chroma value greater than 1.5 is an even number
        self.find_nominal_c(2.6)
        self.assertTrue(self.is_even(self.myMunsell.Nominal_C))
        self.find_nominal_c(11.2)
        self.assertTrue(self.is_even(self.myMunsell.Nominal_C))

    def test_findVerbalForValue(self):
        self.assertEqual("dark", self.myMunsell.findVerbalForValue(3))
        self.assertEqual("light", self.myMunsell.findVerbalForValue(7))
        self.assertEqual("middle", self.myMunsell.findVerbalForValue(4))

    def test_findVerbalForChroma(self):
        self.assertEqual("very weak", self.myMunsell.findVerbalForChroma(1))
        self.assertEqual("moderate", self.myMunsell.findVerbalForChroma(6))


if __name__ == "__main__":
    unittest.main()
