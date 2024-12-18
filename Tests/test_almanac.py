import sys
sys.path.append("..\src")

import almanac
import angle
import unittest

class test_almanac(unittest.TestCase):
    def test_GHAAriesAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmamacGHAAries="245*40.4'"
        almanac.source=0
        apyGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)        

    def test_CelestialObjectGHAAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmanacSunGHA="34*01.8'"
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunGHA=Sun.GHAAt(Y,M,D,h,m,s)        
        self.assertAlmostEqual(apySunGHA,angle.ToDecimal(navAlmanacSunGHA),0)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        localSunGHA=Sun.GHAAt(Y,M,D,h,m,s)        
        self.assertAlmostEqual(localSunGHA,angle.ToDecimal(navAlmanacSunGHA),2)

    def test_CelestialObjectDecAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmanacDec="5*07.3'"
        almanac.source=0
        Venus=almanac.GetCelestialObject("Venus")
        apyVenusDec=Venus.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVenusDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Venus=almanac.GetCelestialObject("Venus")
        locVenusDec=Venus.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVenusDec,angle.ToDecimal(navAlmanacDec),2)
    
    def test_CelestialObjectSHAAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmanacSHA="80*34.1'"
        almanac.source=0
        Vega=almanac.GetCelestialObject("Vega")
        apyVegaSHA=Vega.SHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVegaSHA,angle.ToDecimal(navAlmanacSHA),0)
        almanac.source=1
        Vega=almanac.GetCelestialObject("Vega")
        locVegaSHA=Vega.SHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVegaSHA,angle.ToDecimal(navAlmanacSHA),0)

    def test_CelestialObjectSDAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunSD=Sun.SDAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apySunSD,0.26834671721778003,6)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        locSunSD=Sun.SDAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locSunSD,0.2683500719405951,6)

    def test_CelestialObjectHPAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunHP=Sun.HPAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apySunHP,0.002457908579812472,6)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        locSunHP=Sun.HPAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locSunHP,0.002457908579812472,6)

if __name__ == '__main__':
    unittest.main()
