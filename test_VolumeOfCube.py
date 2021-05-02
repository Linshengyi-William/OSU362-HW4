import unittest
import VolumeOfCube

inp =(input("Please enter a positive, non-zero integer: "))
class TestCase_input(unittest.TestCase):
    def test_positiveInput(self):
        self.assertGreater(int(inp),0)
    def test_typeInput(self):
        self.assertEqual(type(int(inp)), type(1))

class TestCase_result(unittest.TestCase):
    def test_isResultRight(self):
        inpp=int(inp)
        self.assertEqual(VolumeOfCube.voc(inp), inpp*inpp*inpp)
    




if __name__ == '__main__':unittest.main()


