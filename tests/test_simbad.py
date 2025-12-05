import setup

import simbad
import unittest

class test_simbad(unittest.TestCase):
    def test_LoadDataFor(self):
        alpha,delta,mu_alpha,mu_delta=simbad.LoadDataFor("Vega")
        self.assertAlmostEqual(alpha,279.23473479,6)
        self.assertAlmostEqual(delta,38.78368896,6)
        self.assertAlmostEqual(mu_alpha,200.94,6)
        self.assertAlmostEqual(mu_delta,286.23,6)

    def test_LoadHPIdFor(self):
        hpId=simbad.LoadHPIdFor("Vega")
        self.assertEqual(hpId,91262)

if __name__ == '__main__':
    unittest.main()
