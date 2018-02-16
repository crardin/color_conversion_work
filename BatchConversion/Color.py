class Color:
    __colorIdentifier = ''
    __colorName = ''
    __illuminantName = 'D50 and 2 degree observer'

    def __init__(self, identifier, colorName):
        self.__colorIdentifier = identifier
        self.__colorName = colorName

    @property
    def colorIdentifier(self):
        return self.__colorIdentifier

    @property
    def colorName(self):
        return self.__colorName

    @property
    def illuminantName(self):
        return self.__illuminantName
