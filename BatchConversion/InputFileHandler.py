import pandas as pd
from FileHandler import FileHandler
from LABColor import LABColor


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
        df = pd.read_csv(self.__inputFileName, quotechar='"', encoding='latin1')
        headerValues = list(df.columns.values)
        uniqueHeaderValues = [s for s in headerValues if "Unique" in s]
        uniqueHeader = ""
        nameHeader = ""
        if len(uniqueHeaderValues) > 0:
            uniqueHeader = uniqueHeaderValues[0]

        nameHeaderValues = [s for s in headerValues if "Name" in s]
        if len(nameHeaderValues) > 0:
            nameHeader = nameHeaderValues[0]

        for index, row in df.iterrows():
            if uniqueHeader != "" and nameHeader != "":
                newColor = LABColor(row[uniqueHeader], row[nameHeader], row['L*'], row['a*'], row['b*'])
            elif nameHeader != "":
                newColor = LABColor(0, row[nameHeader], row['L*'], row['a*'], row['b*'])
            self.__colors.append(newColor)

    @property
    def Colors(self):
        self.getInputData()
        return self.__colors

    @property
    def inputFileName(self):
        return self.__inputFileName

    @inputFileName.setter
    def inputFileName(self, value):
        self.__inputFileName = value

