#HMIS demo unitest
import unittest
#Returns the characters of 'string1' not included in 'string2'
def characters_not_included(p1, p2):
    return "".join(set(p1).difference(set(p2)))


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
