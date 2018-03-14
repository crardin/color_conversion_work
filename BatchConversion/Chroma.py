class Chroma:
    """
    class to handle Munsell Chroma information
    """
    __CValue = 0.0
    __CNominalValue = 0.0

    def __init__(self, value):
        self.__CValue = value

    def findNominalValue(self):
        if self.__CValue <= 0.5:
            self.__CNominalValue = 0
        if 1.5 >= self.__CValue > 0.5:
            self.__CNominalValue = 1
        if self.__CValue > 1.5:
            vals = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            value = lambda myvalue: min(vals, key=lambda x: abs(x - myvalue))
            self.__CNominalValue = value(self.__CValue)

    @property
    def C(self):
        return self.__CValue

    @C.setter
    def C(self, value):
        self.__CValue = value

    @property
    def NominalC(self):
        self.findNominalValue()
        return self.__CNominalValue
