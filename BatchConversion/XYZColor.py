from Illuminant import Illuminant
import math


class XYZColor:
    __L = 0
    __A = 0
    __B = 0
    __X = 0
    __Y = 0
    __Z = 0
    __yr = 0
    __xyzVector = []
    __delta = 6 / 29.0
    # added the division by 100 to get the "Normalized" values of the illuminant vector
    [Xn, Yn, Zn] = [x/100.0 for x in Illuminant().illuminantVector]

    def __init__(self, L, A, B):
        self.__L = L
        self.__A = A
        self.__B = B
        self.calculateXYZVector()

    def checkDelta(self, t):
        returnValue = 0.0
        if t > self.__delta:
            returnValue = t**3
        else:
            returnValue = 3.0 * self.__delta**2 * (t - (4 / 29))
            # returnValue = (t - 16/116)/7.787

        return round(returnValue, 3)

    def calculate_Yr(self):
        self.__yr = (self.__L + 16) / 116

    def calculateX(self):
        t = self.__yr + (self.__A / 500.0)
        self.__X = round(self.Xn * self.checkDelta(t), 3)

    def calculateY(self):
        t = self.__yr
        self.__Y = round(self.Yn * self.checkDelta(t), 3)

    def calculateZ(self):
        t = (self.__yr - (self.__B / 200))
        self.__Z = round(self.Zn * self.checkDelta(t), 3)

    def calculateXYZVector(self):
        self.calculate_Yr()
        self.calculateX()
        self.calculateY()
        self.calculateZ()
        self.__xyzVector = [self.__X, self.__Y, self.__Z]

    @property
    def xyzVector(self):
        self.calculateXYZVector()
        return self.__xyzVector

    @property
    def X(self):
        return self.__X

    @property
    def Y(self):
        return self.__Y

    @property
    def Z(self):
        return self.__Z

    @property
    def L(self):
        return self.__L

    @L.setter
    def L(self, value):
        self.__L = value

    @property
    def Yr(self):
        return self.__yr
