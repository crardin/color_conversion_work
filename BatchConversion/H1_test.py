import unittest
from BatchConversion.H1 import H1


class TestH1(unittest.TestCase):
    def setUp(self):
        self.myH1 = H1(7.1)

    def test_H1_value(self):
        self.assertEqual(7.1, self.myH1.H1)

    def test_H1_nominal_value(self):
        self.assertEqual(7.5, self.myH1.NominalH1)

    def test_H1_lower_edge_case(self):
        self.myH1.H1 = 0.0
        self.assertEqual(2.5, self.myH1.NominalH1)

    def test_H1_nominal_upper_edge_case(self):
        self.myH1.H1 = 10.0
        self.assertEqual(10.0, self.myH1.NominalH1)


if __name__ == "__main__":
    unittest.main()