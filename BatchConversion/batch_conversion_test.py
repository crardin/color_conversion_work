import unittest
from BatchConversion.batch_conversion import BatchConverter


class testBatchConverter(unittest.TestCase):
    def setUp(self):
        # self.inputFile = '../InputData/C&DColors.csv'
        self.inputFile = '../InputData/test.csv'
        self.outputFile = '../Output/transformedValues.csv'
        self.myConverter = BatchConverter()
        self.myConverter.inputFileName = self.inputFile

    def test_training_data_existence(self):
        self.assertEqual(1625, len(self.myConverter.labTrainingValues))
        self.assertEqual(1625, len(self.myConverter.munsellTrainingValues))

    def test_input_file_name_setter(self):
        self.assertEqual(self.inputFile, self.myConverter.inputFileName)

    def test_input_colors_list_length(self):
        self.assertEqual(93, len(self.myConverter.colors))

    def test_output_file_name_setter(self):
        self.myConverter.outputFileName = self.outputFile
        self.assertEqual(self.outputFile, self.myConverter.outputFileName)

    def test_first_input_lab_value(self):
        self.assertEqual('33.563 0.4 -4.525', self.myConverter.colors[0].LABColor)

    def test_last_input_lab_value(self):
        self.assertEqual('48.153 10.639000000000001 23.272', self.myConverter.colors[len(self.myConverter.colors) - 1].LABColor)

    def test_first_predicted_value(self):
        self.assertEqual(6.5, self.myConverter.predictedColors[0]['H1'])
        self.assertEqual('PB', self.myConverter.predictedColors[0]['H2'])
        self.assertEqual(3, self.myConverter.predictedColors[0]['V'])
        self.assertEqual(1, self.myConverter.predictedColors[0]['C'])

    def test_last_predicted_value(self):
        index = len(self.myConverter.predictedColors) - 1
        self.assertEqual(8.0, self.myConverter.predictedColors[index]['H1'])
        self.assertEqual('YR', self.myConverter.predictedColors[index]['H2'])
        self.assertEqual(5, self.myConverter.predictedColors[index]['V'])
        self.assertEqual(5, self.myConverter.predictedColors[index]['C'])


if __name__ == "__main__":
    unittest.main()
