from pysettings import conf
import settings
conf+=settings

import pyforms
from pyforms import BaseWidget

from pyforms.Controls import ControlEmptyWidget
from BatchConverterWindow import BatchConverterWindow
from singleColorConversionWindow import SingleConverterWindow

class BaseWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Color Converter')

        self.mainmenu = [
            {'File': [
                {'Batch Transform': self.__batchTransformEvent},
                {'Single Color Transform': self.__singleColorTransformEvent},
                # {'Load Illuminant Data': self.__loadIlluminantDataEvent},
                # {'Load Reference Data': self.__loadReferenceDataEvent},
                # {'Current Settings': self.__currentSettingsEvent},
                # {'Show Reference Color Space': self.__showColorSpaceEvent},
                {'Exit': self.__exit}
            ]
            }
        ]

        self._panel = ControlEmptyWidget()
        self._panel.value = BatchConverterWindow()

    def __batchTransformEvent(self):
        win = BatchConverterWindow()
        win.parent = self
        self._panel.value = win

    def __singleColorTransformEvent(self):
        win = SingleConverterWindow()
        win.parent = self
        self._panel.value = win

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


if __name__ == "__main__":
    pyforms.start_app(BaseWindow)