class FileHandler(object):
    """
    class to handle file handling
    """

    __fileName = ""
    __inputFile = None

    def __init__(self):
        pass

    def openFile(self):
        self.__inputFile = open(self.__fileName)

    def closeFile(self):
        self.inputFile.close()

    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, value):
        self.__fileName = value

    @property
    def inputFile(self):
        return self.__inputFile

    @inputFile.setter
    def inputFile(self, value):
        self.__inputFile = value



