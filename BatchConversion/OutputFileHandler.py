import os
import csv
from BatchConversion.FileHandler import FileHandler


class OutputFileHandler(FileHandler):
    """
    class to handle outputing data to a given output file
    """
    __colors = []
    __outputFileName = ""

    def __init__(self, outputFileName):
        FileHandler.__init__(self)
        self.__outputFileName = outputFileName

    def outputColorsToFile(self):
        outputFile = open(self.__outputFileName, 'w', newline='')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(['Unique #', 'Label', 'L', 'a', 'b', 'Munsell', 'H1', 'H2', 'V', 'C'])

    @property
    def OutputFileName(self):
        return self.__outputFileName

    @OutputFileName.setter
    def OutputFileName(self, value):
        if os.path.isdir(value):
            self.__outputFileName = str(value)

    @property
    def OutputColors(self):
        return self.__colors

    @OutputColors.setter
    def OutputColors(self, value):
        self.__colors = value
