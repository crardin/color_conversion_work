import csv
import pandas as pd
# from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from BatchConversion.Munsell import Munsell
from BatchConversion.LABColor import LABColor


class BatchConverter(object):
    __inputFileName = '../InputData/C&DColors.csv'
    # __inputFileName = '../InputData/TestWithoutAnswers.csv'
    __outputFileName = '../Output/transformedValues.csv'
    __colors = []
    __predictedColors = []

    def __init__(self):
        self.clf = None
        self.neigh = KNeighborsClassifier(n_neighbors=1)
        self.myMunsell = Munsell()
        self.trainData()

    def trainData(self):
        self.neigh.fit(self.myMunsell.labValues, self.myMunsell.munsellValues)
        # self.clf = svm.SVC()
        # self.clf.fit(self.myMunsell.labValues, self.myMunsell.HValues)
        # self.clf2 = svm.SVC()
        # self.clf2.fit(self.myMunsell.labValues, self.myMunsell.VValues)
        # self.clf3 = svm.SVC()
        # self.clf3.fit(self.myMunsell.labValues, self.myMunsell.CValues)

    def testDataTraining(self):
        # test values
        print(self.clf.predict([[10.63, 12.59, -2.07]]))  # should be 10RP 1/2
        print(self.clf.predict([[10.63, -7.8, 1.3]]))  # should be 7.5G 1/2

    def getInputData(self):
        df = pd.read_csv(self.__inputFileName, names=["OriginalName", "L*", "a*", "b*"], quotechar='"', encoding='latin1')
        for index, row in df[1:].iterrows():
            newColor = LABColor(0, row['OriginalName'], row['L*'], row['a*'], row['b*'])
            self.__colors.append(newColor)

    def predictData(self):
        self.__predictedColors = []
        for currentColor in self.__colors:
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
        for color in self.__colors:
            calculatedValues = color.CalculatedMunsellList
            outputWriter.writerow(
                [color.colorIdentifier, color.colorName, color.LabList[0], color.LabList[1], color.LabList[2],
                 self.neigh.predict([color.LabList]), calculatedValues[0], calculatedValues[1], calculatedValues[2],
                 calculatedValues[3]])
        outputFile.close()

    @property
    def predictedColors(self):
        return self.__predictedColors

    @property
    def colors(self):
        return self.__colors

    @property
    def inputFileName(self):
        return self.__inputFileName

    @inputFileName.setter
    def inputFileName(self, value):
        self.__inputFileName = value
        self.inputFile = open(self.__inputFileName)

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
