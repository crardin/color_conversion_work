from FileHandler import FileHandler
import pandas as pd
import numpy as np


class JuddFileHandler(FileHandler):
    """
    class to handle importing Judd conversion information
    """
    __juddFileName = "Judd.xlsx"
    __juddData = []
    __juddCategory = 0
    __juddVerbal = ""
    __nominalMunsell = []
    __Munsell = []
    __df = None
    __dE = 0
    __h2mask = []

    def __init__(self):
        FileHandler.__init__(self)
        self.importJuddData()

    def importJuddData(self):
        self.__df = pd.read_excel(self.__juddFileName)

    def getCandidates(self):
        h2 = self.__Munsell[1]
        self.__h2mask = self.__df['CentroidH2'] == h2

    def getJuddCategory(self):
        self.getCandidates()
        h1Candidates = self.__df[self.__h2mask]['CentroidH1']
        h1 = self.__Munsell[0]
        self.findNearest(h1Candidates, h1)

    def getJuddVerbal(self, idx):
        self.__juddVerbal = self.__df[idx]['VerbalDescription']

    def findNearest(self, array, value):
        idx = (np.abs(array - value)).argmin()
        self.__juddCategory = array[idx]
        # self.getJuddVerbal(idx)

    @property
    def JuddFileName(self):
        return self.__juddFileName

    @property
    def JuddCategory(self):
        self.getJuddCategory()
        return self.__juddCategory

    @property
    def JuddVerbal(self):
        return self.__juddVerbal

    @property
    def deltaE(self):
        return self.__dE

    @deltaE.setter
    def deltaE(self, value):
        self.__dE = value

    @property
    def Munsell(self):
        return self.__Munsell

    @Munsell.setter
    def Munsell(self, value):
        self.__Munsell = value

    @property
    def NominalMunsell(self):
        return self.__nominalMunsell

    @NominalMunsell.setter
    def NominalMunsell(self, value):
        self.__nominalMunsell = value


if __name__ == "__main__":
    myJudd = JuddFileHandler()
    myJudd.Munsell = [5.1, 'PB', 9.1, 5]
    print(myJudd.JuddCategory)
    # print(myJudd.JuddVerbal)
