import math
import numpy as np
from BatchConversion.Color import Color
from BatchConversion.Munsell import Munsell


class LABColor(Color):
    """
    class  to represent a given Lab color
    """
    __L = 0
    __a = 0
    __b = 0
    __NominalLabVector = []
    __roundedLab = ''
    __LChVector = []
    __Munsell = None
    __MunsellVector = []
    __NominalMunsellVector = []
    __HueNumber = 0.0
    __HueLetter = ''
    __Value = 0.0
    __Chroma = 0.0
    __DeltaE = 0.0
    __fortyHue = 0.0

    def __init__(self, colorIdentifier, colorName, L, a, b):
        Color.__init__(self, colorIdentifier, colorName)
        self.checkLabValue(L, a, b)
        self.convertLabToLCh()
        self.convertLabToMunsell()

    def checkLabValue(self, L, a, b):
        try:
            self.__L = float(L)
            self.__L = round(self.__L, 2)
        except (ValueError, TypeError):
            print("Value is not a float")
        try:
            self.__a = float(a)
            self.__a = round(self.__a, 2)
        except (ValueError, TypeError):
            print("Value is not a float")
        try:
            self.__b = float(b)
            self.__b = round(self.__b, 2)
        except (ValueError, TypeError):
            print("Value is not a float")

    def convertLabToLCh(self):
        C = self.calculateChromaValue()
        h = self.calculateHueValue()
        self.__LChVector = [self.__L, C, h]

    def calculateFortyHue(self):
        self.__fortyHue = self.deltaE / 2.5
        self.__fortyHue = int(round(self.__fortyHue, 0))

    def calculateDeltaE(self):
        """
        this method is going to utilize the CIE76 method of calculating the deltaE value
        it is also known as deltaE*_ab

        there are more modern versions to calculating this number

        :return: deltaE value for the given LABColor
        """
        self.convertNominalMunsellToLab()
        self.__DeltaE = math.sqrt(
            self.delta(self.LabVector[0], self.NominalLabVector[0]) + self.delta(self.LabVector[1],
                                                                                 self.NominalLabVector[1]) + self.delta(
                self.LabVector[2], self.NominalLabVector[2]))
        self.__DeltaE = round(self.__DeltaE, 2)

    @staticmethod
    def delta(input1, input2):
        """
        static function to find the difference of two numbers squared
        :param input1: first number
        :param input2: second number
        :return: take the difference of the two numbers and square the results
        """
        returnValue = 0.0

        if isinstance(input1, float) and isinstance(input2, float):
            if input1 > input2:
                returnValue = math.pow((input1 - input2), 2)
            else:
                returnValue = math.pow((input2 - input1), 2)

        returnValue = round(returnValue, 2)

        return returnValue

    def convertNominalMunsellToLab(self):
        """
        function to convert a Munsell vector to a Lab vector
        :return: a nominal Lab vector
        """
        L = self.NominalMunsellVector[1] * 10
        C = self.NominalMunsellVector[2] * 5
        h = self.findHueNumber()

        a = C * math.cos(h)
        b = C * math.sin(h)

        self.NominalLabVector = [L, a, b]

    def findHueNumber(self):
        """
        function to find an approximate value for the hue angle from a munsell value
        :return: an angle in radians
        """
        hueLetterCode = self.findHueLetterCode(self.NominalMunsellVector[1])
        SingleHueNumber = divmod(divmod(17 - hueLetterCode, 10)[0] + (self.NominalMunsellVector[0]/10.0) - 0.5, 10)[0]
        returnAngleDegrees = np.interp(SingleHueNumber, [0, 2, 3, 4, 5, 6, 8, 9, 10],
                                       [0, 45, 70, 135, 160, 225, 255, 315, 360])
        return returnAngleDegrees

    @staticmethod
    def findHueLetterCode(inputHueLetter):
        colors = {'R': 6, 'YR': 5, 'Y': 4, 'GY': 3, 'G': 2, 'BG': 1, 'B': 0, 'PB': 9, 'P': 8, 'RP': 7,
                  'N': -2.5}
        if inputHueLetter in colors:
            return colors[inputHueLetter]

    def calculateHueValue(self):
        h = math.atan2(self.__b, self.__a)
        h = math.degrees(h)
        if h < 0:
            h += 360.0
        elif h >= 360:
            h -= 360.0
        h = round(h, 2)
        return h

    def calculateChromaValue(self):
        C = math.sqrt(pow(self.__a, 2) + pow(self.__b, 2))
        C = round(C, 2)
        return C

    def getHueLetter(self):
        """
         The Munsell hues are assumed to be evenly spaced on a circle, with 5Y
         at 90 degrees, 5G at 162 degrees, and so on.  Each letter code corresponds
         to a certain sector of the circle.  The following cases extract the
         letter code.
        :param
        :return: A letter code based on the input angle
        """
        inputAngle = self.LChVector[2]

        if inputAngle == 0:
            HueLetterCode = 'RP'
        elif inputAngle <= 36:
            HueLetterCode = 'R'
        elif inputAngle <= 72:
            HueLetterCode = 'YR'
        elif inputAngle <= 108:
            HueLetterCode = 'Y'
        elif inputAngle <= 144:
            HueLetterCode = 'GY'
        elif inputAngle <= 180:
            HueLetterCode = 'G'
        elif inputAngle <= 216:
            HueLetterCode = 'BG'
        elif inputAngle <= 252:
            HueLetterCode = 'B'
        elif inputAngle <= 288:
            HueLetterCode = 'PB'
        elif inputAngle <= 324:
            HueLetterCode = 'P'
        else:
            HueLetterCode = 'RP'
        self.__HueLetter = HueLetterCode

    def getHueNumber(self):
        """
            Each letter code is prefixed by a number greater than 0, and less than
            or equal to 10, that further specifies the hue.
            :return: Number between 0 and 10
        """
        xp = np.linspace(0, 36)
        fp = np.linspace(0, 10)
        HueNumber = round(np.interp(divmod(self.LChVector[2], 36)[1], xp, fp), 1)
        self.__HueNumber = HueNumber

    def convertLabToMunsell(self):
        """
        method to perform conversion to the Munsell Color representation
        """
        self.__Munsell = Munsell(self.HueNumber, self.HueLetter, self.Value, self.Chroma)

    def calculateChroma(self):
        self.__Chroma = round((self.LChVector[1] / 5.0), 1)

    def calculateValue(self):
        returnValue = self.LChVector[0] / 10.0
        returnValue = round(returnValue, 1)
        self.__Value = returnValue

    @property
    def LABColor(self):
        return str(self.__L) + " " + str(self.__a) + " " + str(self.__b)

    @property
    def HueNumber(self):
        self.getHueNumber()
        return self.__HueNumber

    @property
    def HueLetter(self):
        self.getHueLetter()
        return self.__HueLetter

    @property
    def Value(self):
        self.calculateValue()
        return self.__Value

    @property
    def Chroma(self):
        self.calculateChroma()
        return self.__Chroma

    @property
    def LabVector(self):
        return [self.__L, self.__a, self.__b]

    @property
    def NominalLabVector(self):
        self.convertNominalMunsellToLab()
        return self.__NominalLabVector

    @NominalLabVector.setter
    def NominalLabVector(self, value):
        self.__NominalLabVector = value

    @property
    def LChVector(self):
        return self.__LChVector

    @property
    def MunsellVector(self):
        return self.__Munsell.MunsellVector

    @property
    def MunsellValue(self):
        return self.__Munsell.MunsellValue

    @property
    def NominalMunsellValue(self):
        return self.__Munsell.NominalMunsellValue

    @property
    def NominalMunsellVector(self):
        return self.__Munsell.NominalMunsellVector

    @property
    def DecimalHue(self):
        return self.__Munsell.DecimalHue

    @property
    def NominalDecimalHue(self):
        return self.__Munsell.NominalDecimalHue

    @property
    def roundedLab(self):
        self.__roundedLab = 'L{0} A{1} B{2}'.format(str(round(self.__L)), str(round(self.__a)), str(round(self.__b)))
        return self.__roundedLab

    @property
    def deltaE(self):
        self.calculateDeltaE()
        return self.__DeltaE

    @property
    def FortyHue(self):
        self.calculateFortyHue()
        return self.__fortyHue