from Color import Color


class RGBColor(Color):
    """
    class to handle sRGB information for a given color
    """
    __RValue = 0.0
    __GValue = 0.0
    __BValue = 0.0

    def __init__(self):
        pass

    def calculateRGBValue(self):
        pass

    @property
    def RGBValue(self):
        self.calculateRGBValue()
        return [self.__RValue, self.__GValue, self.__BValue]
