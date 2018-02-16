class menuFunctionality(object):
    def __init__(self):
        self.mainmenu.append(
            {'File': [
                {'Batch Transform': self.__batchTransformEvent},
                {'Single Color Transform': self.__singleColorTransformEvent},
                {'Load Illuminant Data': self.__loadIlluminantDataEvent},
                {'Load Reference Data': self.__loadReferenceDataEvent},
                {'Current Settings': self.__currentSettingsEvent},
                {'Show Reference Color Space': self.__showColorSpaceEvent},
                {'Exit': self.__exit}
                ]
            }
        )

    def __batchTransformEvent(self):
        pass

    def __singleColorTransformEvent(self):
        pass

    def __loadIlluminantDataEvent(self):
        pass

    def __loadReferenceDataEvent(self):
        pass

    def __currentSettingsEvent(self):
        pass

    def __showColorSpaceEvent(self):
        pass

    def __exit(self):
        exit()
