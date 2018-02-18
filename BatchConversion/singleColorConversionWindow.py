import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlLabel
from pyforms.Controls import ControlText
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton

class SingleConverterWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Single Color Converter')
        self.parent = None
        self._inputType = ControlCombo('Input Value Type')
        self._inputType.add_item('L*a*b*', 'Lab')
        self._inputType.add_item('Munsell', 'Munsell')
        self._inputValue1 = ControlText('L*')
        self._inputValue2 = ControlText('a*')
        self._inputValue3 = ControlText('b*')
        self._colorValue = ControlLabel()
        self._outputValue = ControlText('OutputValue')
        self._transformButton = ControlButton('Transform')
        self._transformButton.value = self.__transformButtonAction
        self.formset = [(['_inputType', '_inputValue1', '_inputValue2', '_inputValue3', '_colorValue'], '_outputValue'), ('_transformButton', ' ')]

        self._inputType.changed_event = self.setInputFields

    def setInputFields(self):
        if self._inputType.value == 'Munsell':
            self._inputValue1.label = 'H'
            self._inputValue2.label = 'V'
            self._inputValue3.label = 'C'
        else:
            self._inputValue1.label = 'L*'
            self._inputValue2.label = 'a*'
            self._inputValue3.label = 'b*'

    def __transformButtonAction(self):
        pass

if __name__ == '__main__':
    pyforms.start_app(SingleConverterWindow)