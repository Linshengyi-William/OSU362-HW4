import unittest
import fullName

fn = input("Please enter the first name: ")
ln = input("Please enter the last name: ")

class TestCase(unittest.TestCase):
    # Test is there space in between first name and last name
    # Passing condition: There is space in name
    # Failing condition: There is no space in name
    def test_space(self):
        name = fullName.fullName(fn, ln)
        self.assertTrue(" " in name)
    # Test is there any number in the name
    # Passing condition: There are no numbers in the name
    # Failing condition: There is number in the name
    def test_isNumber(self):
        name = fullName.fullName(fn, ln)
        self.assertFalse(any(num.isdigit() for num in name))
    # Test if the name is invalidly too long
    # Passing condition: The name is no longer than 500 characters.
    # Failing condition: The name is longer or equal to 500 characters.
    def test_length(self):
        name = fullName.fullName(fn, ln)
        self.assertLess(len(name),500)

if __name__ == '__main__':unittest.main()


