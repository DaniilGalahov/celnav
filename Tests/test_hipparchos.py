import sys
sys.path.append("..\src")

import hipparcos
import unittest

class test_hipparcos(unittest.TestCase):
    def test_LoadDataFor(self):
        alpha,delta,mu_alpha,mu_delta=hipparcos.LoadDataFor(91262)
        self.assertAlmostEqual(alpha,279.23410832,6)
        self.assertAlmostEqual(delta,38.78299311,6)
        self.assertAlmostEqual(mu_alpha,201.02,6)
        self.assertAlmostEqual(mu_delta,287.46,6)

if __name__ == '__main__':
    unittest.main()
