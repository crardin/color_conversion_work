import math


class xyYColor:
    __X = 0
    __Y = 0
    __Z = 0
    __x = 0
    __y = 0
    __H1 = 0.0
    __H2 = ""
    __Value = 0.0
    __Chroma = 0.0
    __luminanceFactor = 0.0
    __valueDifferenceThreshold = 0.001
    __valueMinus = 0.0
    __valuePlus = 0.0
    __JuddCategory = ''
    __JuddVerbal = ''

    # def __init__(self, X, Y, Z):
    #     self.__X = X
    #     self.__Y = Y
    #     self.__Z = Z

    def __init__(self, H1, H2, Value, Chroma):
        self.__H1 = H1
        self.__H2 = H2
        self.__Value = Value
        self.__Chroma = Chroma

    def calculateX(self):
        self.__x = self.__X / (self.__X + self.__Y + self.__Z)

    def calculateY(self):
        self.__y = self.__Y / (self.__X + self.__Y + self.__Z)

    def convertMunsellToxyY(self):
        self.__Y = self.LuminanceFactor
        if math.fabs(self.__Value - round(self.__Value)) < self.__valueDifferenceThreshold:
            self.__valueMinus = round(self.__Value)
            self.__valuePlus = round(self.__Value)
        else:
            self.__valueMinus = math.floor(self.__Value)
            self.__valuePlus = self.__valueMinus + 1

    def findJuddCategory(self):
        pass

    def findJuddVerbal(self):
        pass

    def calculateASTMD1535LuminanceFactor(self):
        term1 = 1.1914 * self.__Value
        term2 = -0.23111 * math.pow(self.__Value, 2)
        term3 = -0.23951 * math.pow(self.__Value, 3)
        term4 = -0.021009 * math.pow(self.__Value, 4)
        term5 = 0.0008404 * math.pow(self.__Value, 5)
        self.__luminanceFactor = term1 + term2 + term3 + term4 + term5

    @property
    def xyYVector(self):
        self.calculateX()
        self.calculateY()
        return [self.__x, self.__y, self.__Y]

    @property
    def LuminanceFactor(self):
        self.calculateASTMD1535LuminanceFactor()
        return self.__luminanceFactor

    @property
    def JuddCategory(self):
        self.findJuddCategory()
        return self.__JuddCategory

    @property
    def JuddVerbal(self):
        self.findJuddVerbal()
        return self.__JuddVerbal
