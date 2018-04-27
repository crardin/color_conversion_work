# from pysettings import conf
# from BatchConversion import settings
#
# conf += settings

import pyforms
from PyQt5.QtWidgets import QFileDialog, QApplication, QHeaderView
from pyforms import BaseWidget
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlList
from pyforms.Controls import ControlLabel
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
        self._messageLabel = ControlLabel('')
        self._LabList = ControlList('Transform Results')
        self._LabList.horizontal_headers = ['Color Name', 'L', 'a', 'b', 'Rounded Lab', 'H1', 'H2', 'V', 'C',
                                            'Nominal Munsell', 'sRGB', 'Hex']
        self._headers = self._LabList.tableWidget.horizontalHeader()
        self._headers.setSectionResizeMode(QHeaderView.Stretch)
        self._headers.setStretchLastSection(False)
        self._LabList.readonly = True
        self._LabList.tableWidget.setAlternatingRowColors(True)

        self.formset = [(' ', '_inputFile', ' '), (' ', '_transformButton', '_saveButton', ' '), '_LabList',
                        (' ', '_messageLabel', ' ')]

    def __transformButtonAction(self):
        self._messageLabel.value = 'Processing Color'
        QApplication.processEvents()
        self.inputFileName = self._inputFile.value
        if self.inputFileName is not None and self.inputFileName != '':
            self._LabList.clear()
            for color in BatchConverter.inputLabColors.fget(self):
                listOutput = [color.colorName, color.LabVector[0], color.LabVector[1], color.LabVector[2],
                              color.roundedLab, color.MunsellVector[0], color.MunsellVector[1], color.MunsellVector[2],
                              color.MunsellVector[3], color.NominalMunsellValue, color.sRGB, color.Hex]
                self._LabList += listOutput
            self._headers.resizeSections(QHeaderView.Stretch)
            # self._LabList.tableWidget.resizeColumnsToContents()
            self._messageLabel.value = 'File Transform Complete'
        else:
            self._messageLabel.value = 'File Transform Failed'
        QApplication.processEvents()

    def __saveButtonAction(self):
        self._messageLabel.value = 'Exporting Color Data'
        QApplication.processEvents()
        self.inputFileName = self._inputFile.value
        if self.inputFileName is not None and self.inputFileName != '':
            self.outputFileName = QFileDialog.getSaveFileName(self, 'Choose Output File')[0]
            BatchConverter.outputData(self)
            self._messageLabel.value = 'File Export Complete'
        else:
            self._messageLabel.value = 'File Export Failed'
        QApplication.processEvents()


if __name__ == '__main__':
    pyforms.start_app(BatchConverterWindow, geometry=(200, 200, 1300, 400))
