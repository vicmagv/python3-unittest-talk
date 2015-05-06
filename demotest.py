import unittest
from example import *

class DemoClassTest(unittest.TestCase):

    a= 'hola asdfadf '
    b= 'perro'
    c= 'gato'

    @classmethod
    def setUpClass(self):
        print('Test starting...')

    def tearDown(self):
        print('bye test :(')

    def test_both_empty(self):
        self.assertEqual( characters_not_included('',''), '' )

    def test_same_string(self):
        self.assertTrue( characters_not_included(self.a, self.a) == '')

    def test_given_strings(self):
        self.assertSetEqual( set(characters_not_included(self.b, self.c)), set('per') )


if __name__ == '__main__':
    unittest.main()
