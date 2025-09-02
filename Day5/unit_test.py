import unittest

def add(a, b):
    return a+b

class TestAdd(unittest.TestCase):
    def test_check(self):
        self.assertTrue(add(3, 4), 7)
    def test_check_false(self):
        self.assertFalse(add(4, 5), 9)

if __name__ == '__main__':
    unittest.main()

    # 9, 8