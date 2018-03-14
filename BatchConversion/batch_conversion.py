import csv
import openpyxl
from sklearn.neighbors import KNeighborsClassifier

from BatchConversion.InputFileHandler import InputFileHandler


class BatchConverter(object):
    """
    class to handle all the batch conversion functions

    should hold instances of the various color classes
    """
    __labTrainingValues = []
    __munsellTrainingValues = []
    __conversionData = {}
    __munsellDataFile = "real_CIELAB.xlsx"
    __inputFileName = ''
    __outputFileName = ''
    __inputLABColors = []
    __predictedColors = []
    __inputFileHandler = None
    __outputFileHandler = None

    def __init__(self):
        self.neigh = KNeighborsClassifier(n_neighbors=1)
        self.getTrainingData()
        self.trainData()

    def trainData(self):
        self.neigh.fit(self.__labTrainingValues, self.__munsellTrainingValues)

    def getTrainingData(self):
        self.__labTrainingValues = []
        self.__munsellTrainingValues = []
        wb = openpyxl.load_workbook(self.__munsellDataFile)
        sheet = wb['data']
        for i in range(2, sheet.max_row + 1):
            munsellValue = self.getMunsellTrainingValue(i, sheet)
            labValue = self.getLabTrainingValue(i, sheet)
            self.__conversionData[labValue] = munsellValue

    def getMunsellTrainingValue(self, i, sheet):
        H = sheet.cell(row=i, column=2).value
        munsellValue = str(H) + " "
        V = sheet.cell(row=i, column=3).value
        munsellValue += str(V) + "/"
        C = sheet.cell(row=i, column=4).value
        munsellValue += str(C)
        self.__munsellTrainingValues.append(str(H + " " + str(V) + "/" + str(C)))
        return munsellValue

    def getLabTrainingValue(self, i, sheet):
        L = sheet.cell(row=i, column=11).value
        labValue = str(L) + " "
        A = sheet.cell(row=i, column=12).value
        labValue += str(A) + " "
        B = sheet.cell(row=i, column=13).value
        labValue += str(B)
        self.__labTrainingValues.append([L, A, B])
        return labValue

    def getInputData(self):
        self.__inputFileHandler.getInputData()
        self.__inputLABColors = self.__inputFileHandler.Colors
        self.predictData()

    def predictData(self):
        self.__predictedColors = []
        for currentColor in self.__inputLABColors:
            calculatedValues = currentColor.CalculatedMunsellList
            currentColor = {'colorName': currentColor.colorName, 'L': currentColor.LabList[0], 'A': currentColor.LabList[1],
                            'B': currentColor.LabList[2], 'colorValue': self.neigh.predict([currentColor.LabList])[0],
                            'H1': calculatedValues[0], 'H2': calculatedValues[1], 'V': calculatedValues[2],
                            'C': calculatedValues[3]}
            self.__predictedColors.append(currentColor)

    def outputData(self):
        outputFile = open(self.outputFileName, 'w', newline='')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(['Unique #', 'Label', 'L', 'a', 'b', 'Munsell', 'H1', 'H2', 'V', 'C'])
        for outputColor in self.__inputLABColors:
            calculatedValues = outputColor.CalculatedMunsellList
            outputWriter.writerow(
                [outputColor.colorIdentifier, outputColor.colorName, outputColor.LabList[0], outputColor.LabList[1], outputColor.LabList[2],
                 self.neigh.predict([outputColor.LabList]), calculatedValues[0], calculatedValues[1], calculatedValues[2],
                 calculatedValues[3]])
        outputFile.close()

    @property
    def conversionData(self):
        return self.__conversionData

    @property
    def labTrainingValues(self):
        return self.__labTrainingValues

    @property
    def munsellTrainingValues(self):
        return self.__munsellTrainingValues

    @property
    def predictedColors(self):
        return self.__predictedColors

    @property
    def colors(self):
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


if __name__ == '__main__':
    myBatchConverter = BatchConverter()
    myBatchConverter.inputFileName = '../InputData/test.csv'
    myBatchConverter.getInputData()
    myBatchConverter.predictData()
    for color in myBatchConverter.predictedColors:
        print(color)
    for color in myBatchConverter.colors:
        print(color.CalculatedMunsellList)
