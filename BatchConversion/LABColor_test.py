import unittest
from LABColor import LABColor


class TestLABColor(unittest.TestCase):
    def setUp(self):
        # cadet blue (5.1PB 4.6/9.1) Nominal(5PB 5/10)
        self.testColor_1 = LABColor(1, "cadet blue", 46.38, -2.155, -36.979)
        # cadmium yellow (2.5Y 7.7/12) Nominal(2.5Y 8/12)
        self.testColor_2 = LABColor(2, 'cadmium yellow', 78, 11, 80)
        # cameo violet (6RP 4.5/3.3) Nominal(5RP 5/4)
        self.testColor_3 = LABColor(3, 'cameo violet', 45.557, 16.351, -0.612)
        # from training data (10RP 1/2)
        self.testColor_4 = LABColor(4, 'test color', 10.63, 12.59, -2.07)
        # from training data (7.5RP 1/6)
        self.testColor_5 = LABColor(5, 'test color 2', 10.63, 28.38, -8.98)

    def test_roundedLAB(self):
        """
            input lab color 82.5 -14.2 43.9
            should return L82 A-14 B44
        """
        inputLabColor = LABColor(4, "input color", 82.5, -14.2, 43.9)
        self.assertEqual('L82 A-14 B44', inputLabColor.roundedLab)

    def test_generateLChVector(self):
        self.assertEqual([46.38, 37.04, 266.67], self.testColor_1.LChVector)
        self.assertEqual([78.00, 80.75, 82.17], self.testColor_2.LChVector)
        self.assertEqual([45.56, 16.36, 357.86], self.testColor_3.LChVector)

    def test_getHueNumber(self):
        self.assertGreaterEqual(self.testColor_1.HueNumber, 0.0)
        self.assertLessEqual(self.testColor_1.HueNumber, 10.0)
        self.assertAlmostEqual(5.1, self.testColor_1.HueNumber, delta=2.0)
        self.assertAlmostEqual(2.5, self.testColor_2.HueNumber, delta=2.0)
        self.assertAlmostEqual(6, self.testColor_3.HueNumber, delta=4.0)
        self.assertAlmostEqual(10, self.testColor_4.HueNumber, delta=4.0)
        self.assertAlmostEqual(7.5, self.testColor_5.HueNumber, delta=3.0)

    def test_MunsellVector(self):
        self.assertGreaterEqual(len(self.testColor_1.MunsellVector), 0)
        self.assertEqual(len(self.testColor_1.MunsellVector), 4)

    def test_deltaE(self):
        self.assertEqual(6.12, self.testColor_1.deltaE)

    def test_delta(self):
        self.assertEqual(1, self.testColor_1.delta(3.0, 2.0))

    def test_findHueLetterCode(self):
        self.assertEqual(4, self.testColor_1.findHueLetterCode('Y'))

    def test_findHueNumber(self):
        self.assertIn(self.testColor_1.findHueNumber(), [0, 45, 70, 135, 160, 225, 255, 315, 360])

    def test_findHueNumber_returnsFloat(self):
        self.assertIsInstance(self.testColor_1.findHueNumber(), float)


if __name__ == "__main__":
    unittest.main()
