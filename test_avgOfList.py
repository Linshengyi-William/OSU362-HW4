import unittest
import avgOfList

lst_1=[1,2,3,4,5,6,7,8]
lst_2=[]
lst_3=["this","is","a","list"]

class TestCase(unittest.TestCase):
    # Test if the aol() returns the right result
    # Passing condition: the result of aol() and the right result are equal.
    # Failing condition: the result of aol() and the right result are not equal.
    def test_rightResult(self):
        self.assertEqual(avgOfList.aol(lst_1), sum(lst_1)/len(lst_1))
    # Test if the list is empty
    # Passing condition: list is not empty
    # Failing condition: list is empty
    def test_emptyList(self):
        self.assertEqual(len(lst_2), 0)
    # Test if the all the element in the list have the type int
    # Passing condition: All the elements in the list have the datatype int
    # Failing condition: At least one of the element in the list doesn't have the datatype int. 
    def test_elementType(self):
        check = False
        for i in range(0,len(lst_3)):
            if type(lst_3[i])==type("str"):
                check = True
        self.assertFalse(check)

if __name__ == '__main__':unittest.main()

