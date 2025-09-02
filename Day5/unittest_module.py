import unittest

def addFunction(a, b):
    return a+b

class TestFucntion(unittest.TestCase):
    def setUp(self):
        print("set up in first class test")
    def test_check_positive(self):
        self.assertEqual(addFunction(3,4), 7)
    def test_check_pos_neg(self):
        self.assertEqual(addFunction(-2, 4), 2)

    def test_cheak_wrong_value(self):
        self.assertNotEqual(addFunction(4,5), 8)
    def test_check_bool(self):
        self.assertTrue('A'.isupper())



class TestFixtures(unittest.TestCase):
    def setUp(self):
        print("set up fixture")
        self.a = 4
        self.b = 5
        self.res = addFunction(self.a, self.b)
    def tearDown(self):
        print('tear down fixture')

    def test_check_positive(self):
        self.assertEqual(self.res, 9)

    def test_check_pos_neg(self):
        self.assertEqual(self.res, 9)

    def test_cheak_wrong_value(self):
        self.assertNotEqual(4, 8)

    def test_check_bool(self):
        self.assertTrue('A'.isupper())

if __name__ == '__main__':
    unittest.main()