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
        with open(self.__outputFileName, 'w', newline='') as outputFile:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(['Unique #', 'Label', 'L', 'a', 'b', 'RoundedLab', 'H1', 'H2', 'V', 'C'])
            for outputColor in self.OutputColors:
                outputWriter.writerow([outputColor.colorIdentifier, outputColor.colorName, outputColor.LabVector[0],
                                      outputColor.LabVector[1], outputColor.LabVector[2], outputColor.roundedLab,
                                      outputColor.MunsellVector[0], outputColor.MunsellVector[1],
                                      outputColor.MunsellVector[2], outputColor.MunsellVector[3]])

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
