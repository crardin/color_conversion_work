from Illuminant import Illuminant


class XYZColor:
    __L = 0
    __A = 0
    __B = 0
    __X = 0
    __Y = 0
    __Z = 0
    __xyzVector = []
    __delta = 0.206893
    [Xn, Yn, Zn] = Illuminant().illuminantVector

    def __init__(self, L, A, B):
        self.__L = L
        self.__A = A
        self.__B = B

    def checkDelta(self, t):
        if t > self.__delta:
            return t ** 3.0
        else:
            # return 3.0 * (self.__delta ** 2.0) * (t - (4 / 29))
            return ((t - 16) / 116) / 7.787

    def calculateX(self):
        t = self.Xn * (((self.__L + 16) / 116) + (self.__A / 500))
        self.__X = self.checkDelta(t)

    def calculateY(self):
        t = self.Yn * ((self.__L + 16) / 116)
        self.__Y = self.checkDelta(t)

    def calculateZ(self):
        t = self.Zn * (((self.__L + 16) / 116) - (self.__B / 200))
        self.__Z = self.checkDelta(t)

    @property
    def xyzVector(self):
        self.calculateX()
        self.calculateY()
        self.calculateZ()
        return [self.__X, self.__Y, self.__Z]
