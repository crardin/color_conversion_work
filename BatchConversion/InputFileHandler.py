import pandas as pd
from BatchConversion.FileHandler import FileHandler
from BatchConversion.LABColor import LABColor
from BatchConversion.Munsell import Munsell


class InputFileHandler(FileHandler):
    """
    class to handle input file data from user
    """
    __colors = []
    __inputFileName = ""

    def __init__(self, inputFileName):
        FileHandler.__init__(self)
        self.__inputFileName = inputFileName

    def getInputData(self):
        self.__colors = []
        self.df = pd.read_csv(self.__inputFileName, quotechar='"', encoding='latin1')
        for index, row in self.df[1:].iterrows():
            if self.determineUniqueColumnIsThere():
                newColor = LABColor(row['Unique #'], row['Name'], row['L*'], row['a*'], row['b*'])
            else:
                newColor = LABColor(0, row['OriginalName'], row['L*'], row['a*'], row['b*'])
            self.__colors.append(newColor)

    def determineUniqueColumnIsThere(self):
        if 'Unique #' in self.df:
            return True
        else:
            return False

    @property
    def Colors(self):
        return self.__colors

    @property
    def inputFileName(self):
        return self.__inputFileName

    @inputFileName.setter
    def inputFileName(self, value):
        self.__inputFileName = value