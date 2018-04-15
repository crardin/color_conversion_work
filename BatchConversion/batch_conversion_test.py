import unittest
from batch_conversion import BatchConverter
from LABColor import LABColor


class testBatchConverter(unittest.TestCase):
    def setUp(self):
        # self.inputFile = '../InputData/C&DColors.csv'
        self.inputFile = '../InputData/test.csv'
        self.outputFile = '../Output/transformedValues.csv'
        self.myConverter = BatchConverter()
        self.myConverter.inputFileName = self.inputFile

    def test_input_file_name_setter(self):
        self.assertEqual(self.inputFile, self.myConverter.inputFileName)

    def test_input_colors_list_length(self):
        self.assertEqual(94, len(self.myConverter.inputLabColors))

    def test_output_file_name_setter(self):
        self.myConverter.outputFileName = self.outputFile
        self.assertEqual(self.outputFile, self.myConverter.outputFileName)

    def test_inputDataColors(self):
        self.assertGreater(len(self.myConverter.inputLabColors), 0)
        self.assertIsInstance(self.myConverter.inputLabColors, list)

    def test_munsellValues(self):
        self.assertGreater(len(self.myConverter.munsellValues), 0)
        self.assertIsInstance(self.myConverter.munsellValues, list)


if __name__ == "__main__":
    unittest.main()
