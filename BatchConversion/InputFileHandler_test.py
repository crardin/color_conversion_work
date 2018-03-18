import unittest
from BatchConversion.InputFileHandler import InputFileHandler


class TestInputFileHandler(unittest.TestCase):
    def setUp(self):
        pass

    def test_getInputData_no_unique_number(self):
        myFileHandler = InputFileHandler('../InputData/test.csv')
        myFileHandler.getInputData()
        self.assertEqual(94, len(myFileHandler.Colors))

    def test_getInputData_unique_number(self):
        myFileHandler = InputFileHandler('../InputData/C&DColors.csv')
        myFileHandler.getInputData()
        self.assertEqual(394, len(myFileHandler.Colors))


if __name__ == "__main__":
    unittest.main()
