from FileHandler import FileHandler
import pandas as pd


class VerbalFileHandler(FileHandler):
    """
    class to handle input of Verbal Data
    """
    _df = None
    _inputFileName = ""

    def __init__(self, inputFileName):
        FileHandler.__init__(self)
        self._inputFileName = inputFileName
        self.importVerbalData()

    def importVerbalData(self):
        self._df = pd.read_excel(self._inputFileName)

    def getHueVerbal(self, h1, h2):
        h1mask = self._df['NominalH1'] == h1
        h2mask = self._df['NominalH2'] == h2
        hueVerbal = self._df[h1mask][h2mask]['text'].values[0]
        return hueVerbal

    @property
    def inputFileName(self):
        return self._inputFileName

    @inputFileName.setter
    def inputFileName(self, value):
        self._inputFileName = value


if __name__ == "__main__":
    myVerbal = VerbalFileHandler("HueVerbalsTable.xlsx")
    print(myVerbal.getHueVerbal(2.5, 'Y'))
