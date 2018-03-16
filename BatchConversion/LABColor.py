import math
import numpy as np
from BatchConversion.Color import Color


class LABColor(Color):
    __L = 0
    __A = 0
    __B = 0
    __H1 = ""
    __H2 = ""
    __V = 0
    __C = 0
    __roundedLab = ''
    __XYZVector = []
    __xyYVector = []
    __LChList = []
    __MunsellVector = []
    __HueNumber = 0

    def __init__(self, colorIdentifier, colorName, L, A, B):
        Color.__init__(self, colorIdentifier, colorName)

        try:
            self.__L = float(L)
        except (ValueError, TypeError):
            print("Value is not a float")
        try:
            self.__A = float(A)
        except (ValueError, TypeError):
            print("Value is not a float")
        try:
            self.__B = float(B)
        except (ValueError, TypeError):
            print("Value is not a float")

    def getAnswerFromFile(self, H1, H2, V, C):
        self.__H1 = H1
        self.__H2 = H2
        self.__V = V
        self.__C = C

    def generateLChList(self):
        C = math.sqrt(math.pow(self.__A, 2) + math.pow(self.__B, 2))
        h = math.atan2(self.__B, self.__A)
        h = math.degrees(h)
        if h < 0:
            h += 360.0
        elif h >= 360:
            h -= 360.0
        self.__LChList = [round(self.__L, 2), round(C, 2), round(h, 2)]

    def getHueLetterCode(self):
        """
         The Munsell hues are assumed to be evenly spaced on a circle, with 5Y
         at 90 degrees, 5G at 162 degrees, and so on.  Each letter code corresponds
         to a certain sector of the circle.  The following cases extract the
         letter code.
        :param inputAngle:
        :return: A letter code based on the input angle
        """
        inputAngle = self.LChList[2]

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
        return HueLetterCode

    def checkIncreasing(self, sequence):
        if np.all(np.diff(sequence) > 0):
            return True
        return False

    def getHueNumber(self):
        """
            Each letter code is prefixed by a number greater than 0, and less than
            or equal to 10, that further specifies the hue.
            :return: Number between 0 and 10
        """
        inputAngleDegrees = self.LChList[2]
        xp = np.linspace(0, 36)
        fp = np.linspace(0, 10)
        HueNumber = round(np.interp(divmod(inputAngleDegrees, 36)[1], xp, fp), 2)
        # if HueNumber <= 0.5:
        #     HueNumber = 10
        self.__HueNumber = HueNumber

    def roundToNearestValue(self, inputValue):
        return round(inputValue * 2) / 2

    def generateMunsellVector(self):
        HueLetter = self.getHueLetterCode()
        Value = self.__LChList[0] / 10.0
        outputValue = round(Value)
        Chroma = (self.__LChList[1]) / 5.0
        outputChroma = round(Chroma)
        if outputChroma <= 0.5:
            outputChroma = 'N'
        self.__MunsellVector = [self.roundToNearestValue(self.HueNumber), HueLetter, outputValue, outputChroma]

    def convertMunsellVectorToStandardSpecification(self):
        pass

    @property
    def LABColor(self):
        return str(self.__L) + " " + str(self.__A) + " " + str(self.__B)

    @property
    def HueNumber(self):
        self.getHueNumber()
        return self.__HueNumber

    @property
    def LabList(self):
        return [self.__L, self.__A, self.__B]

    @property
    def LChList(self):
        self.generateLChList()
        return self.__LChList

    @LChList.setter
    def LChList(self, value):
        self.__LChList = value

    @property
    def MunsellVector(self):
        self.generateLChList()
        self.generateMunsellVector()
        return self.__MunsellVector

    @property
    def roundedLab(self):
        self.__roundedLab = 'L{0} A{1} B{2}'.format(str(round(self.__L)), str(round(self.__A)), str(round(self.__B)))
        return self.__roundedLab

    @property
    def testAnswer(self):
        return self.__H1 + self.__H2 + " " + str(self.__V) + "/" + str(self.__C)

    @property
    def XYZVector(self):
        return self.__XYZVector

    @property
    def xyYVector(self):
        return self.__xyYVector
