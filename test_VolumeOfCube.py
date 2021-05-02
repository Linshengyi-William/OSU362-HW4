import unittest
import VolumeOfCube

inp =(input("Please enter a positive, non-zero integer: "))
class TestCase_input(unittest.TestCase):
    # Test if the input is positive
    # Passing condition: The input is a positive number
    # Failing condition: The input isn't a positive number
    def test_positiveInput(self):
        self.assertGreater(int(inp),0)
    # Test if the type of the input is int
    # Passing condition: The input have the datatype int
    # Failing condition: The input don't have the datatype int
    def test_typeInput(self):
        self.assertEqual(type(int(inp)), type(1))

class TestCase_result(unittest.TestCase):
    # Test if the result is right
    # Passing condition: The result is right.
    # Failing condition: The result is wrong.
    def test_isResultRight(self):
        inpp=int(inp)
        self.assertEqual(VolumeOfCube.voc(inp), inpp*inpp*inpp)
    




if __name__ == '__main__':unittest.main()


