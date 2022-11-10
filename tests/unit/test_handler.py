import unittest
from hello_world import app

class calculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(5,3),8)
    def test_sub(self):
        self.assertEqual(app.sub(5,3),2)
    def test_mul(self):
        self.assertEqual(app.mul(5,3),15)
    def test_div(self):
        self.assertEqual(app.div(4,2),2)

if __name__ == '__main__':
    unittest.main()