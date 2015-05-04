import unittest
from example import *

class TestClass1(unittest.TestCase): #test case
    a = "asdlfkjasdlkfjalsdfña"

    def setUp(self):
        print('comienza el test! :)')

    def tearDown(self):
        print('acaba el test :(')

    def test_all_empty(self):
        self.assertTrue( characters_not_included("","") ==  "" )

    def test_same_words(self):
        self.assertTrue( characters_not_included(self.a,self.a) == "" )

    def test_first_empty(self):
        self.assertTrue( characters_not_included("",self.a) == "")

    def test_second_empty(self):
        self.assertTrue( set(characters_not_included(self.a,"")) == set(self.a) )


if __name__ == '__main__':
    unittest.main()
