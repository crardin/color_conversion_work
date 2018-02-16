from Color import Color


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

        # self.__XYZVector = XYZColor(self.__L, self.__A, self.__B).xyzVector
        # self.__xyYVector = xyYColor(self.__XYZVector[0], self.__XYZVector[1], self.__XYZVector[2]).xyYVector

    def getAnswerFromFile(self, H1, H2, V, C):
        self.__H1 = H1
        self.__H2 = H2
        self.__V = V
        self.__C = C

    @property
    def LABColor(self):
        return str(self.__L) + " " + str(self.__A) + " " + str(self.__B)

    @property
    def LabList(self):
        return [self.__L, self.__A, self.__B]

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
