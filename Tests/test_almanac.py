import sys
sys.path.append("..")

import almanac
import angle
import unittest

class test_almanac(unittest.TestCase):
    def test_GHAAriesAt(self):
        time='2023-10-27 14:00:00'
        navAlmamacGHAAries="245*40.4'"
        almanac.source=0
        apyGHAAries=almanac.GHAOfAriesAt(time)
        self.assertAlmostEqual(apyGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(time)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)        

    def test_CelestialObjectGHAAt(self):
        time='2023-10-27 14:00:00'
        navAlmanacSunGHA="34*01.8'"
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunGHA=Sun.GHAAt(time)        
        self.assertAlmostEqual(apySunGHA,angle.ToDecimal(navAlmanacSunGHA),0)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        localSunGHA=Sun.GHAAt(time)        
        self.assertAlmostEqual(localSunGHA,angle.ToDecimal(navAlmanacSunGHA),2)

    def test_CelestialObjectDecAt(self):
        time='2023-10-27 14:00:00'
        navAlmanacDec="5*07.3'"
        almanac.source=0
        Venus=almanac.GetCelestialObject("Venus")
        apyVenusDec=Venus.DecAt(time)
        self.assertAlmostEqual(apyVenusDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Venus=almanac.GetCelestialObject("Venus")
        locVenusDec=Venus.DecAt(time)
        self.assertAlmostEqual(locVenusDec,angle.ToDecimal(navAlmanacDec),2)
    
    def test_CelestialObjectSHAAt(self):
        time='2023-10-27 14:00:00'
        navAlmanacSHA="80*34.1'"
        almanac.source=0
        Vega=almanac.GetCelestialObject("Vega")
        apyVegaSHA=Vega.SHAAt(time)
        self.assertAlmostEqual(apyVegaSHA,angle.ToDecimal(navAlmanacSHA),0)
        almanac.source=1
        Vega=almanac.GetCelestialObject("Vega")
        locVegaSHA=Vega.SHAAt(time)
        self.assertAlmostEqual(locVegaSHA,angle.ToDecimal(navAlmanacSHA),0)

    def test_CelestialObjectSDAt(self):
        time='2023-10-27 14:00:00'
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunSD=Sun.SDAt(time)
        self.assertAlmostEqual(apySunSD,0.26834671721778003,6)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        locSunSD=Sun.SDAt(time)
        self.assertAlmostEqual(locSunSD,0.2683500719405951,6)

    def test_CelestialObjectHPAt(self):
        time='2023-10-27 14:00:00'
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunHP=Sun.HPAt(time)
        self.assertAlmostEqual(apySunHP,0.002457908579812472,6)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        locSunHP=Sun.HPAt(time)
        self.assertAlmostEqual(locSunHP,0.002457908579812472,6)

if __name__ == '__main__':
    unittest.main()
