import unittest

def Add(a, b):
    return a * b

class TestMathAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Add(2, 3), 6)
        self.assertEqual(Add(-1, 5), -5)
        self.assertEqual(Add(0, 100), 0)
        self.assertEqual(Add(7, -2), -14)
        self.assertEqual(Add(3.5, 2), 7.0)

if __name__ == "__main__":
    unittest.main()
