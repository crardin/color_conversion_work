
class xyYColor:
    __X = 0
    __Y = 0
    __Z = 0
    __x = 0
    __y = 0

    def __init__(self, X, Y, Z):
        self.__X = X
        self.__Y = Y
        self.__Z = Z

    def calculateX(self):
        self.__x = self.__X / (self.__X + self.__Y + self.__Z)

    def calculateY(self):
        self.__y = self.__Y / (self.__X + self.__Y + self.__Z)

    @property
    def xyYVector(self):
        self.calculateX()
        self.calculateY()
        return [self.__x, self.__y, self.__Y]
