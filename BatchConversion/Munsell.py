class Munsell:
    """
    class to handle data related to a Munsell color
    """
    __H1 = 0.0
    __H2 = ''
    __V = 0.0
    __C = 0.0
    __DecimalHue = 0.0
    __NominalDecimalHue = 0.0
    __Nominal_H1 = 0.0
    __Nominal_V = 0
    __Nominal_C = 0
    __NominalMunsellVector = []
    __MunsellVector = []

    def __init__(self, HueNumber, HueLetter, Value, Chroma):
        self.__H1 = round(HueNumber, 2)
        self.__H2 = HueLetter
        self.__V = round(Value, 2)
        self.__C = round(Chroma, 2)
        self.__MunsellVector = [self.__H1, self.__H2, self.__V, self.__C]

    @staticmethod
    def getNumberForHueLetter(inputHueLetter):
        colors = {'R': 0, 'YR': 10, 'Y': 20, 'GY': 30, 'G': 40, 'BG': 50, 'B': 60, 'PB': 70, 'P': 80, 'RP': 90,
                  'N': -2.5}
        if inputHueLetter in colors:
            return colors[inputHueLetter]

    def calculateDecimalHue(self):
        h1 = self.MunsellVector[0]
        h2 = self.getNumberForHueLetter(self.MunsellVector[1])
        self.__DecimalHue = h1 + h2

    def calculateNominalDecimalHue(self):
        h1 = self.NominalMunsellVector[0]
        h2 = self.getNumberForHueLetter(self.NominalMunsellVector[1])
        self.__NominalDecimalHue = h1 + h2

    def findNominalMunsell(self):
        self.findNominalH1()
        self.findNominalValue()
        self.findNominalChroma()
        self.__NominalMunsellVector = [self.__Nominal_H1, self.__H2, self.__Nominal_V, self.__Nominal_C]

    def findNominalH1(self):
        # must be 2.5, 5, 7.5, or 10
        vals = [2.5, 5, 7.5, 10]
        value = lambda myvalue: min(vals, key=lambda x: abs(x - myvalue))
        self.__Nominal_H1 = value(self.__H1)

    def findNominalValue(self):
        # should return a whole number between 1 and 10
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        value = lambda myvalue: min(vals, key=lambda x: abs(x - myvalue))
        self.__Nominal_V = value(self.__V)

    def findNominalChroma(self):
        if self.__C <= 0.5:
            self.__Nominal_C = 0
        if 1.5 >= self.__C > 0.5:
            self.__Nominal_C = 1
        if self.__C > 1.5:
            vals = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            value = lambda myvalue: min(vals, key=lambda x: abs(x - myvalue))
            self.__Nominal_C = value(self.__C)

    @staticmethod
    def formatMunsellString(inputVector):
        return str(inputVector[0]) + inputVector[1] + ' ' + str(inputVector[2]) + '/' + str(inputVector[3])

    @property
    def MunsellVector(self):
        return [self.__H1, self.__H2, self.__V, self.__C]

    @property
    def MunsellValue(self):
        return self.formatMunsellString(self.MunsellVector)

    @property
    def NominalMunsellVector(self):
        self.findNominalMunsell()
        return self.__NominalMunsellVector

    @property
    def NominalMunsellValue(self):
        return self.formatMunsellString(self.NominalMunsellVector)

    @property
    def DecimalHue(self):
        self.calculateDecimalHue()
        return self.__DecimalHue

    @property
    def NominalDecimalHue(self):
        self.calculateNominalDecimalHue()
        return self.__NominalDecimalHue

    @property
    def H1(self):
        return self.__H1

    @H1.setter
    def H1(self, value):
        self.__H1 = value

    @property
    def H2(self):
        return self.__H2

    @H2.setter
    def H2(self, value):
        self.__H2 = value

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, value):
        self.__V = value

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        self.__C = value


if __name__ == "__main__":
    pass