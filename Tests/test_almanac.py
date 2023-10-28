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

    def test_CelestialObjectGHAAt(self):
        time='2023-10-27T14:00:00'

        Sun=almanac.GetCelestialObject("Sun")
        navAlmanacSunGHA="34*01.8'"
        self.assertAlmostEqual(Sun.GHAAt(time),angle.ToDecimal(navAlmanacSunGHA),6)

    def test_CelestialObjectDecAt(self):
        time='2023-10-27T14:00:00'
        
        Venus=almanac.GetCelestialObject("Venus")
        navAlmanacDec="5*07.3'"
        self.assertAlmostEqual(Venus.DecAt(time),angle.ToDecimal(navAlmanacDec),6)
    
    def test_CelestialObjectSHAAt(self):
        time='2023-10-27T14:00:00'
        
        Vega=almanac.GetCelestialObject("Vega")
        navAlmanacSHA="80*34.1'"
        self.assertAlmostEqual(Vega.SHAAt(time),angle.ToDecimal(navAlmanacSHA),6)

    def test_CelestialObjectSDAt(self):
        time='2023-10-27T14:00:00'
        
        Sun=almanac.GetCelestialObject("Sun")
        self.assertAlmostEqual(Sun.SDAt(time),0.26834671721778003,6)

    def test_CelestialObjectHPAt(self):
        time='2023-10-27T14:00:00'
        
        Sun=almanac.GetCelestialObject("Sun")
        self.assertAlmostEqual(Sun.HPAt(time),0.0024551582322560246,6)

if __name__ == '__main__':
    unittest.main()
