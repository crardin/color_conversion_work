class H2:
    """
    class to handle Munsell H2 data
    """
    __H2Value = ""
    __H2NumberValue = 0.0
    __H2NominalValue = ""

    def __init__(self, value):
        self.__H2Value = value

    def findNominalValue(self):
        self.__H2NominalValue = self.__H2Value

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

    def getHueNumber(self):
        if self.__H2Value == 'R':
            self.__H2NumberValue = 0
        elif self.__H2Value == 'YR':
            self.__H2NumberValue = 10
        elif self.__H2Value == 'Y':
            self.__H2NumberValue = 20
        elif self.__H2Value == 'GY':
            self.__H2NumberValue = 30
        elif self.__H2Value == 'G':
            self.__H2NumberValue = 40
        elif self.__H2Value == 'BG':
            self.__H2NumberValue = 50
        elif self.__H2Value == 'B':
            self.__H2NumberValue = 60
        elif self.__H2Value == 'PB':
            self.__H2NumberValue = 70
        elif self.__H2Value == 'P':
            self.__H2NumberValue = 80
        elif self.__H2Value == 'RP':
            self.__H2NumberValue = 90
        elif self.__H2Value == 'N':
            self.__H2NumberValue = -2.5

    @property
    def H2(self):
        return self.__H2Value

    @property
    def NominalH2(self):
        self.findNominalValue()
        return self.__H2NominalValue

    @property
    def NumericH2(self):
        self.getHueNumber()
        return self.__H2NumberValue
