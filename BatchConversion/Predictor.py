import re
import openpyxl
from sklearn.neighbors import KNeighborsClassifier


class Predictor:
    __munsellDataFile = "real_CIELAB.xlsx"
    __conversionData = {}
    __munsellTrainingValues = []
    __labTrainingValues = []

    def __init__(self):
        self.neigh = KNeighborsClassifier(n_neighbors=1)
        self.getTrainingData()
        self.trainData()

    def getTrainingData(self):
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
        a = sheet.cell(row=i, column=12).value
        labValue += str(a) + " "
        b = sheet.cell(row=i, column=13).value
        labValue += str(b)
        self.__labTrainingValues.append([L, a, b])
        return labValue

    def trainData(self):
        self.neigh.fit(self.__labTrainingValues, self.__munsellTrainingValues)

    def getMunsellValue(self, inputString):
        inputString.strip()
        splitString = re.findall('(\d+\.?\d|\d+|\w+)', inputString)
        splitString[0] = float(splitString[0])
        splitString[2] = int(splitString[2])
        splitString[3] = int(splitString[3])
        return splitString

    def predictNominalMunsellVector(self, LabVector):
        predictedValue = self.neigh.predict([LabVector])[0]
        return self.getMunsellValue(predictedValue)


if __name__ == "__main__":
    myPredictor = Predictor()
