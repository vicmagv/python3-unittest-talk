import unittest
from example import *

class TestClass1(unittest.TestCase): #test case

    def test_all_empty(self):
        self.assertTrue( characters_not_included("","") ==  "" )

    def test_same_words(self):
        a = "asdlfkjasdlkfjalsdfña"
        self.assertTrue( characters_not_included(a,a) == "" )

    def test_first_empty(self):
        a = "asdlfkjasdlkfjalsdfña"
        self.assertTrue( characters_not_included("",a) == "")

    def test_second_empty(self):
        a = "asdlfkjasdlkfjalsdfña"
        self.assertTrue( set(characters_not_included(a,"")) == set(a) )


if __name__ == '__main__':
    unittest.main()
