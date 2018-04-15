from InputFileHandler import InputFileHandler
from OutputFileHandler import OutputFileHandler
from Predictor import Predictor


class BatchConverter(object):
    """
    class to handle all the batch conversion functions

    should hold instances of the various color classes
    """
    __inputFileName = ''
    __outputFileName = ''
    __inputLABColors = []
    __munsellValues = []
    __nominalMunsellVectors = []
    __inputFileHandler = None
    __outputFileHandler = None
    __predictor = None

    def __init__(self):
        self.__predictor = Predictor()

    def getInputData(self):
        self.__inputFileHandler.getInputData()
        self.__inputLABColors = self.__inputFileHandler.Colors

    def getMunsellValues(self):
        for currentColor in self.__inputLABColors:
            self.__munsellValues.append(currentColor.MunsellVector)

    def getNominalMunsellVectors(self):
        for currentColor in self.__inputLABColors:
            self.__predictor.predictNominalMunsellVector(currentColor.LabVector)
            self.__nominalMunsellVectors.append(self.__predictor.PredictedMunsellVector)
            currentColor.NominalMunsellVector = self.__predictor.PredictedMunsellVector

    def outputData(self):
        self.__outputFileHandler.OutputColors = self.__inputLABColors
        self.__outputFileHandler.outputColorsToFile()

    @property
    def munsellValues(self):
        self.getMunsellValues()
        return self.__munsellValues

    @property
    def nominalMunsellVectors(self):
        self.getNominalMunsellVectors()
        return self.__nominalMunsellVectors

    @property
    def inputLabColors(self):
        # self.getInputData()
        return self.__inputLABColors

    @property
    def inputFileName(self):
        return self.__inputFileName

    @inputFileName.setter
    def inputFileName(self, value):
        self.__inputFileName = value
        if not self.__inputFileHandler:
            self.__inputFileHandler = InputFileHandler(self.__inputFileName)
        else:
            self.__inputFileHandler.inputFileName = self.__inputFileName
        self.getInputData()
        self.getNominalMunsellVectors()

    @property
    def outputFileName(self):
        return self.__outputFileName

    @outputFileName.setter
    def outputFileName(self, value):
        self.__outputFileName = str(value)
        if value is not None and value != '':
            if not self.__outputFileHandler:
                self.__outputFileHandler = OutputFileHandler(self.__outputFileName)
            else:
                self.__outputFileHandler.outputFileName = self.__outputFileName


if __name__ == '__main__':
    myBatchConverter = BatchConverter()
    myBatchConverter.inputFileName = "../InputData/test.csv"
    myBatchConverter.getInputData()
    print(myBatchConverter.nominalMunsellVectors)
