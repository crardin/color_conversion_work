"""
1. open the input csv file
2. open the output excel file
3. For each line in the file
    3.1 save the Lab value from the line
    3.2 save the Munsell value from the line
    3.3 convert the lab value to Munsell value
    3.4 compare the converted value to the given value
    3.5 output data to an excel file
4. close input file
5. close output file
x6. data structure for all Lab values
x7. data structure for all Munsell given values
x8. data structure for all converted values
9. conversion function caller
    6.1 function that points to a given conversion method
10. comparison function
10. conversion functions

"""
import csv
import openpyxl

givenLabValues = []
givenMunsellValues = []
convertedMunsellValues = []

inputFileName = ""
outputFileName = ""

inputFile = open(inputFileName)

inputFile.close()


