import sys
sys.path.append("..")

import almanac
import angle
import unittest

class test_almanac(unittest.TestCase):
    def test_GHAAriesAt(self):
        time='2023-10-27T14:00:00'
        navAlmamacGHAAries="245*40.4'"
        self.assertAlmostEqual(almanac.GHAOfAriesAt(time),angle.ToDecimal(navAlmamacGHAAries),6)

    def test_CelestialObject(self):
        time='2023-10-27T14:00:00'
        #Vega=almanac.GetCelestialObject("Vega")
        #navAlmanacSHA="80*34.1'"
        #self.assertAlmostEqual(Vega.SHAAt(time),angle.ToDecimal(navAlmanacSHA),6)

        Sun=almanac.GetCelestialObject("Sun")
        navAlmanacSunGHA="34*01.8'"
        self.assertAlmostEqual(Sun.GHAAt(time),angle.ToDecimal(navAlmanacSunGHA),6)

if __name__ == '__main__':
    unittest.main()
