from Color import Color
import numpy as np
import math


class RGBColor(Color):
    """
    class to handle sRGB information for a given color
    """
    __RGBVector = []
    __sRGBVector = []
    __XYZVector = []
    # D65 rotation Matrix
    # __rotationMatrix = [[3.2404542, -1.5371385, -0.4985314], [-0.9692660, 1.8760108, 0.0415560], [0.0556434, -0.2040259, 1.0572252]]
    # D50 rotation Matrix
    __rotationMatrix = [[3.1339, -1.6169, -0.4906], [-0.9788, 1.9161, 0.0335], [0.0720, -0.2290, 1.4052]]

    def __init__(self, X, Y, Z):
        self.__XYZVector = [X, Y, Z]
        self.calculate_RGBVector()

    def calculate_RGBVector(self):
        self.__rotationMatrix = np.array(self.__rotationMatrix)
        self.__XYZVector = np.array(self.__XYZVector)
        self.__RGBVector = np.matmul(self.__rotationMatrix, self.__XYZVector)
        self.__RGBVector = [round(x, 2) for x in self.__RGBVector]

    def gammaCorrectValue(self, inputValue):
        a = 0.055
        if inputValue <= 0.0031308:
            return 12.92 * inputValue
        else:
            return (1 + a) * math.pow(inputValue, 1 / 2.4) - a

    def calculate_sRGBVector(self):
        self.__sRGBVector = [self.gammaCorrectValue(x) for x in self.__RGBVector]
        self.__sRGBVector = np.array(self.__sRGBVector)
        self.__sRGBVector = self.__sRGBVector * 255
        self.__sRGBVector = self.__sRGBVector.astype('int').tolist()

    def clamp(self, value):
        return max(0, min(value, 255))

    @property
    def RGBVector(self):
        self.calculate_RGBVector()
        return self.__RGBVector

    @property
    def sRGBVector(self):
        self.calculate_sRGBVector()
        return self.__sRGBVector

    @property
    def sRGBValue(self):
        return ", ".join(str(x) for x in self.sRGBVector)

    @property
    def hexValue(self):
        r = self.clamp(self.sRGBVector[0])
        g = self.clamp(self.sRGBVector[1])
        b = self.clamp(self.sRGBVector[2])
        hexString = "#{0:02x}{1:02x}{2:02x}".format(r, g, b).upper()
        return hexString
