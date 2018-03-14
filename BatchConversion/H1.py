class H1:
    """
    class to handle Munsell H1 information
    """
    __H1Value = 0.0
    __H1NominalValue = 0.0

    def __init__(self, value):
        self.__H1Value = value

    def findNominalValue(self):
        # must be 2.5, 5, 7.5, or 10
        vals = [2.5, 5, 7.5, 10]
        value = lambda myvalue: min(vals, key=lambda x: abs(x - myvalue))
        self.__H1NominalValue = value(self.__H1Value)

    @property
    def H1(self):
        return self.__H1Value

    @H1.setter
    def H1(self, value):
        self.__H1Value = value

    @property
    def NominalH1(self):
        self.findNominalValue()
        return self.__H1NominalValue
