import unittest
from BatchConversion.batch_conversion import BatchConverter


class testBatchConverter(unittest.TestCase):
    def setUp(self):
        # self.inputFile = '../InputData/C&DColors.csv'
        self.inputFile = '../InputData/test.csv'
        self.myConverter = BatchConverter()
        self.myConverter.inputFileName = self.inputFile

    def test_input_file_name(self):
        self.assertEqual(self.inputFile, self.myConverter.inputFileName)

    def test_colors_list(self):
        self.assertEqual(93, len(self.myConverter.colors))

    def test_first_lab_training_value(self):
        self.assertEqual('33.563 0.4 -4.525', self.myConverter.colors[0].LABColor)

    def test_last_lab_training_value(self):
        self.assertEqual('48.153 10.639000000000001 23.272', self.myConverter.colors[len(self.myConverter.colors) - 1].LABColor)


if __name__ == "__main__":
    unittest.main()
