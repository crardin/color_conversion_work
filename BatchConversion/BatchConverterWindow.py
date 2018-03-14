import re

import pyforms
from AnyQt.QtWidgets import QFileDialog
from pyforms import BaseWidget
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlList

from BatchConversion.batch_conversion import BatchConverter


class BatchConverterWindow(BatchConverter, BaseWidget):
    def __init__(self):
        BatchConverter.__init__(self)
        BaseWidget.__init__(self, 'Batch Converter')
        self.parent = None

        # definition of the forms fields
        self._inputFile = ControlFile('Input File', default='', helptext='choose a file to input batch data from',
                                      use_save_dialog=False)
        self._transformButton = ControlButton('Transform')
        self._transformButton.value = self.__transformButtonAction
        self._saveButton = ControlButton('Export')
        self._saveButton.value = self.__saveButtonAction
        self._LabList = ControlList('Transform Results')
        self._LabList.horizontal_headers = ['Color Name', 'L', 'a', 'b', 'Rounded Lab', 'Fit H1', 'Fit H2', 'Fit V',
                                            'Fit C', 'H1', 'H2', 'V', 'C']
        self._LabList.readonly = True
        self._LabList.tableWidget.resizeColumnsToContents()
        self._LabList.resize_rows_contents()
        self.formset = [(' ', '_inputFile', ' '), (' ', '_transformButton', '_saveButton', ' '), ('_LabList')]

    def getMunsellValues(self, inputString):
        inputString = str(inputString)
        inputString.strip()
        splitString = re.findall('(\d+\.?\d|\d+|\w+)', inputString)
        return splitString

    def __transformButtonAction(self):
        self.inputFileName = self._inputFile.value
        if self.inputFileName is not None and self.inputFileName != '':
            self._LabList.clear()
            BatchConverter.getInputData(self)
            BatchConverter.predictData(self)
            for color in BatchConverter.predictedColors.fget(self):
                munsellValues = self.getMunsellValues(color['colorValue'])
                listOutput = [color['colorName'], color['L'], color['A'], color['B'], color['roundedLab'],
                              munsellValues[0],
                              munsellValues[1], munsellValues[2], munsellValues[3], color['H1'], color['H2'],
                              color['V'], color['C']]
                self._LabList += listOutput
            self._LabList.tableWidget.resizeColumnsToContents()

    def __saveButtonAction(self):
        self.inputFileName = self._inputFile.value
        if self.inputFileName is not None and self.inputFileName != '':
            BatchConverter.getInputData(self)
            BatchConverter.predictData(self)
            self.outputFileName = QFileDialog.getSaveFileName(self, 'Choose Output File')[0]
            print(self.outputFileName)
            if self.outputFileName is not None and self.outputFileName != '':
                BatchConverter.outputData(self)


if __name__ == '__main__':
    pyforms.start_app(BatchConverterWindow)
