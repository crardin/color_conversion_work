class Value:
    """
    class to hold Munsell Value information
    """
    __VValue = 0.0
    __VNominalValue = 0.0

    def __init__(self, value):
        self.__VValue = value

    def findNominalValue(self):
        # should return a whole number between 1 and 10
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        value = lambda myvalue: min(vals, key=lambda x: abs(x - myvalue))
        self.__VNominalValue = value(self.__VValue)

    @property
    def V(self):
        return self.__VValue

    @V.setter
    def V(self, value):
        self.__VValue = value

    @property
    def NominalV(self):
        self.findNominalValue()
        return self.__VNominalValue
