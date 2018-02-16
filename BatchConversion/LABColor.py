import math
import numpy as np
from Color import Color
from XYZColor import XYZColor
from xyYColor import xyYColor


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
    __MunsellList = []

    def __init__(self, colorIdentifier, colorName, L, A, B):
        Color.__init__(self, colorIdentifier, colorName)
        try:
            self.__L = float(L)
        except ValueError:
            print("Value is not a float")
        try:
            self.__A = float(A)
        except ValueError:
            print("Value is not a float")
        try:
            self.__B = float(B)
        except ValueError:
            print("Value is not a float")

        self.__XYZVector = XYZColor(self.__L, self.__A, self.__B).xyzVector
        self.__xyYVector = xyYColor(self.__XYZVector[0], self.__XYZVector[1], self.__XYZVector[2]).xyYVector

    def getAnswerFromFile(self, H1, H2, V, C):
        self.__H1 = H1
        self.__H2 = H2
        self.__V = V
        self.__C = C

    def generateLChList(self):
        C = math.sqrt(math.pow(self.__A, 2) + math.pow(self.__B, 2))
        h = math.atan2(self.__B,self.__A)
        self.__LChList = [self.__L, C, h]

    def getHueLetterCode(self, inputAngle):
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

    def getHueNumber(self, inputAngle):
        HueNumber = np.interp(inputAngle % 36, np.linspace(0, 36, 10), np.linspace(0, 10, 10))
        if HueNumber == 0:
            HueNumber = 10
        return HueNumber

    def generateMunsellList(self):
        habDegrees = self.__LChList[2] * (180/math.pi)
        habDegrees = habDegrees % 360
        HueLetter = self.getHueLetterCode(habDegrees)
        HueNumber = self.getHueNumber(habDegrees)
        Value = self.__LChList[0] / 10.0
        Chroma = (self.__LChList[1]) / 5.0
        if Chroma <= 0.5:
            Chroma = 'N'
        self.__MunsellList = [HueNumber, HueLetter, Value, Chroma]

    @property
    def LABColor(self):
        return str(self.__L) + " " + str(self.__A) + " " + str(self.__B)

    @property
    def LabList(self):
        return [self.__L, self.__A, self.__B]

    @property
    def LChList(self):
        self.generateLChList()
        return self.__LChList

    @property
    def CalculatedMunsellList(self):
        self.generateLChList()
        self.generateMunsellList()
        return self.__MunsellList

    @property
    def roundedLab(self):
        self.__roundedLab = 'L{0} A{1} B{2}'.format(str(round(int(self.__L))), str(round(int(self.__A))),
                                                    str(round(int(self.__B))))
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

