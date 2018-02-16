import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton

class SingleConverterWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Single Color Converter')
        self.parent = None
        self._inputType = ControlCombo('InputType')
        self._inputType.add_item('Lab', 'Lab')
        self._inputType.add_item('Munsell', 'Munsell')
        self._outputType = ControlCombo('OutputType')
        self._outputType.add_item('Lab', 'Lab')
        self._outputType.add_item('Munsell', 'Munsell')
        self._inputValue = ControlText('InputValue')
        self._outputValue = ControlText('OutputValue')
        self._transformButton = ControlButton('Transform')
        self._transformButton.value = self.__transformButtonAction
        self.formset = [('_inputType', '_outputType'), ('_inputValue', '_outputValue'), (' ', '_transformButton')]

    def __transformButtonAction(self):
        pass

if __name__ == '__main__':
    pyforms.start_app(SingleConverterWindow)