import unittest
from XYZColor import XYZColor


class TestXYZColor(unittest.TestCase):
    def setUp(self):
        self.delta = 6/29.0
        # cadet blue (5.1PB 4.6/9.1) Nominal (5PB 5/10)
        # should return the XYZ result
        # X = 0.14429
        # Y = 0.1555
        # Z = 0.411
        # self.myXYZ = XYZColor(46.38, -2.155, -36.979)
        # self.expectedX = 0.14429
        # self.expectedY = 0.1555
        # self.expectedZ = 0.411

        # cadmium yellow (2.5Y 7.7/12) Nominal(2.5Y 8/12)
        # should return the XYZ result
        # X = 0.5560
        # Y = 0.5321
        # Z = 0.0570
        self.myXYZ = XYZColor(78, 11, 80)
        self.expectedX = 0.5560
        self.expectedY = 0.5321
        self.expectedZ = 0.0570

    def test_checkDelta(self):
        """
        should make sure that the delta is being returned correctly
        for a given set of inputs
        """
        t = 0.5
        deltaResult = self.myXYZ.checkDelta(t)
        self.assertEqual(deltaResult, t**3)

        t = 0.1
        deltaResult = self.myXYZ.checkDelta(t)
        self.assertEqual(deltaResult, -0.005)

    def test_calculate_Yr(self):
        self.myXYZ.L = 0.0
        self.myXYZ.calculate_Yr()
        self.assertEqual(4/29.0, self.myXYZ.Yr)

    def test_Y_value_zero_at_zero(self):
        self.myXYZ.L = 0.0
        self.myXYZ.calculate_Yr()
        self.myXYZ.calculateY()
        self.assertEqual(self.myXYZ.Y, 0)

    def test_XYZ_conversion_from_LAB(self):
        # self.assertListEqual(self.myXYZ.xyzVector, [0.144, 0.155, 0.411])
        returnVector = self.myXYZ.xyzVector
        self.assertAlmostEqual(returnVector[0], self.expectedX, delta=0.1)
        self.assertAlmostEqual(returnVector[1], self.expectedY, delta=0.1)
        self.assertAlmostEqual(returnVector[2], self.expectedZ, delta=0.1)


if __name__ == "__main__":
    unittest.main()