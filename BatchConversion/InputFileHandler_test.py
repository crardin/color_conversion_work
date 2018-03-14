import unittest
from BatchConversion.InputFileHandler import InputFileHandler


class TestInputFileHandler(unittest.TestCase):
    def setUp(self):
        pass

    def test_getInputData_no_unique_number(self):
        myFileHandler = InputFileHandler('../InputData/test.csv')
        myFileHandler.getInputData()
        self.assertEqual(93, len(myFileHandler.Colors))

    def test_getInputData_unique_number(self):
        myFileHandler = InputFileHandler('../InputData/C&DColors.csv')
        myFileHandler.getInputData()
        self.assertEqual(393, len(myFileHandler.Colors))

    def test_unique_column_not_there(self):
        # test for if the unique column is not there
        myFileHandler = InputFileHandler('../InputData/test.csv')
        myFileHandler.getInputData()
        self.assertFalse(myFileHandler.determineUniqueColumnIsThere())

    def test_determineUniqueColumnIsThere(self):
        # test for if the Unique # column is there
        myFileHandler = InputFileHandler('../InputData/C&DColors.csv')
        myFileHandler.getInputData()
        self.assertTrue(myFileHandler.determineUniqueColumnIsThere())


if __name__ == "__main__":
    unittest.main()
