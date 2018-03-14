class Munsell:
    """
    class to handle data related to a Munsell color
    """
    __H1 = 0.0
    __H2 = ''
    __V = 0.0
    __C = 0.0

    def __init__(self):
        pass

    @property
    def munsellValue(self):
        return [self.__H1, self.__H2, self.__V, self.__C]

    @property
    def fullMunsellValue(self):
        return str(self.__H1) + str(self.__H2) + ' ' + str(self.__V) + '/' + str(self.__C)

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
    myMunsell = Munsell()

