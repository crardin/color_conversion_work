import unittest
from BatchConversion.LABColor import LABColor


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

    def test_generateLChList(self):
        self.assertEqual([46.38, 37.04, 266.66], self.testColor_1.LChList)
        self.assertEqual([78.00, 80.75, 82.17], self.testColor_2.LChList)
        self.assertEqual([45.56, 16.36, 357.86], self.testColor_3.LChList)

    def test_getHueNumber(self):
        self.assertAlmostEqual(5.1, self.testColor_1.HueNumber, delta=1.0)
        # self.assertAlmostEqual(2.5, self.testColor_2.HueNumber, delta=1.0)
        # self.assertAlmostEqual(6, self.testColor_3.HueNumber, delta=1.0)
        # self.assertAlmostEqual(10, self.testColor_4.HueNumber, delta=1.0)
        # self.assertAlmostEqual(7.5, self.testColor_5.HueNumber, delta=1.0)

    def test_getHueLetterCode(self):
        pass

    def test_generateMunsellVector(self):
        # test of the Munsell Vector generator function
        # putting in the LCh values from above
        # should return 2.5P 4/8
        # LChList = [45.208, 38.99, 306.56]
        # self.myColor.LChList = LChList
        # self.myColor.generateMunsellVector()
        # self.assertEqual([2.5, 'P', 4, 8], self.myColor.MunsellVector)
        pass

    def test_StandardSpecificationFunction(self):
        pass


if __name__ == "__main__":
    unittest.main()
