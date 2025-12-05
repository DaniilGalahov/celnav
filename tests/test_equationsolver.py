import setup

import equationsolver
import unittest

class test_equationsolver(unittest.TestCase):
    def test_LinEq22(self):
        x,y=equationsolver.LinEq22(1,2,3,2,3,1)
        self.assertEqual(x,-7)
        self.assertEqual(y,5)

if __name__ == '__main__':
    unittest.main()
