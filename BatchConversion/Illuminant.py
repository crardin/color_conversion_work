class Illuminant:
    __illuminantIdentifier = 'D50'
    __illuminantDegreeOfVision = '2 degrees'
    __illuminantVector = [96.6797, 100.00, 82.5188]

    def __init__(self):
        pass

    @property
    def illuminantIdentifier(self):
        return self.__illuminantIdentifier

    @property
    def illuminantDegreeOfVision(self):
        return self.__illuminantDegreeOfVision

    @property
    def illuminantVector(self):
        return self.__illuminantVector