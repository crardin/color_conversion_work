import unittest
from RGB import RGBColor


class TestRGB(unittest.TestCase):
    def setUp(self):
        # cadet blue (5.1PB 4.6/9.1) Nominal(5PB 5/10)
        # RGB = 42, 114, 172
        # Hex = #4371AC
        # X, Y, Z = 0.14428, 0.1555, 0.411
        # self.myRGB = RGBColor(0.14429, 0.155, 0.411)
        # self.expectedR = 66
        # self.expectedG = 113
        # self.expectedB = 172
        # self.expectedHex = "#4371AC"

        # cadmium yellow (2.5Y 7.7/12) Nominal(2.5Y 8/12)
        # should return the XYZ result
        # X = 0.5560
        # Y = 0.5321
        # Z = 0.0570
        # self.myXYZ = XYZColor(78, 11, 80)
        # Hex = #EEB800
        self.myRGB = RGBColor(0.5560, 0.5321, 0.0570)
        self.expectedR = 238
        self.expectedG = 184
        self.expectedB = 0
        self.expectedHex = "#EEB800"

    @unittest.skip
    def test_linear_RGB_calculation(self):
        self.assertEqual(self.myRGB.RGBVector[0], 0.02)
        self.assertEqual(self.myRGB.RGBVector[1], 0.17)
        self.assertEqual(self.myRGB.RGBVector[2], 0.41)

    def test_sRGB_calculation(self):
        print(self.myRGB.sRGBVector)
        self.assertAlmostEqual(self.myRGB.sRGBVector[0], self.expectedR, delta=5)
        self.assertAlmostEqual(self.myRGB.sRGBVector[1], self.expectedG, delta=2)
        self.assertAlmostEqual(self.myRGB.sRGBVector[2], self.expectedB, delta=1)

    def test_sRGBValue(self):
        print(self.myRGB.sRGBValue)
        self.assertEqual("237,184,0", self.myRGB.sRGBValue)

    def testHexValue(self):
        self.assertEqual(self.expectedHex, self.myRGB.hexValue)

    def test_gammaCorrectValue_between_0_and_1(self):
        pass


if __name__ == "__main__":
    unittest.main()