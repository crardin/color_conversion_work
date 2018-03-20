from BatchConversion.InputFileHandler import InputFileHandler
from BatchConversion.OutputFileHandler import OutputFileHandler


class BatchConverter(object):
    """
    class to handle all the batch conversion functions

    should hold instances of the various color classes
    """
    __inputFileName = ''
    __outputFileName = ''
    __inputLABColors = []
    __munsellValues = []
    __inputFileHandler = None
    __outputFileHandler = None

    def __init__(self):
        pass

    def getInputData(self):
        self.__inputFileHandler.getInputData()
        self.__inputLABColors = self.__inputFileHandler.Colors

    def getMunsellValues(self):
        for currentColor in self.__inputLABColors:
            self.__munsellValues.append(currentColor.MunsellVector)

    def outputData(self):
        self.__outputFileHandler.OutputColors = self.__inputLABColors
        self.__outputFileHandler.outputColorsToFile()

    @property
    def munsellValues(self):
        self.getMunsellValues()
        return self.__munsellValues

    @property
    def inputLabColors(self):
        self.getInputData()
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
    myBatchConverter.inputFileName = '../InputData/test.csv'
    myBatchConverter.getInputData()
