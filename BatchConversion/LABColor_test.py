import unittest
from BatchConversion.LABColor import LABColor


class TestLABColor(unittest.TestCase):
    def setUp(self):
        self.myColor = LABColor(1, 'test color', 45.208, 23.222, -31.316)

    def test_LABColor(self):
        self.assertEqual('45.208 23.222 -31.316', self.myColor.LABColor)

    def test_roundedLAB(self):
        self.assertEqual('L45 A23 B-31', self.myColor.roundedLab)

    def test_generateLChList(self):
        self.assertEqual([45.208, 38.986576407784256, 306.55833489172625], self.myColor.LChList)

    def test_getHueLetterCode(self):
        inputAngle = 0
        hueLetter = self.myColor.getHueLetterCode(inputAngle)
        self.assertEqual('RP', hueLetter)
        inputAngle = 50
        hueLetter = self.myColor.getHueLetterCode(inputAngle)
        self.assertEqual('YR', hueLetter)
        inputAngle = 330
        hueLetter = self.myColor.getHueLetterCode(inputAngle)
        self.assertEqual('RP', hueLetter)


if __name__ == "__main__":
    unittest.main()
