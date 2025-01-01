import sys
sys.path.append("..\src")

import almanac
import angle
import unittest

class test_almanac(unittest.TestCase):
    #@unittest.skip("For debug pruposes")
    def test_GHAAriesAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0) #initial check to match Nautical Almanac
        navAlmamacGHAAries="245*40.4'"
        almanac.source=0
        apyGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyGHAAries,angle.ToDecimal(navAlmamacGHAAries),2) #so, assertAlmostEqual is rounding compared values to number of decimal places after floating point
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        Y,M,D,h,m,s=(2024,4,12,12,0,0) #additional check to match Nautical Almanac      
        navAlmamacGHAAries="21*10.8'"
        almanac.source=0
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        Y,M,D,h,m,s=(2024,10,27,14,0,0) #third check to match Nautical Almanac       
        navAlmamacGHAAries="246*25.3'"
        almanac.source=0
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        Y,M,D,h,m,s=(2024,12,25,12,0,0) #forth check to match Nautical Almanac
        navAlmamacGHAAries="274*29.6'"
        almanac.source=0
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        Y,M,D,h,m,s=(2024,12,26,6,0,0) #what about values near 180*?
        navAlmamacGHAAries="185*13.9'"
        almanac.source=0
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        Y,M,D,h,m,s=(2024,12,26,18,0,0) #and near 360*?
        navAlmamacGHAAries="5*43.5'"
        almanac.source=0
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)
        almanac.source=1
        localGHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(localGHAAries,angle.ToDecimal(navAlmamacGHAAries),2)

    #@unittest.skip("For debug pruposes")
    def test_CelestialObjectGHAAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmanacSunGHA="34*01.8'"
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunGHA=Sun.GHAAt(Y,M,D,h,m,s)        
        self.assertAlmostEqual(apySunGHA,angle.ToDecimal(navAlmanacSunGHA),0) #can not get better precision from astropy yet
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        localSunGHA=Sun.GHAAt(Y,M,D,h,m,s)        
        self.assertAlmostEqual(localSunGHA,angle.ToDecimal(navAlmanacSunGHA),2)
        Y,M,D,h,m,s=(2024,12,26,0,0,0) #must be checked near 180*
        navAlmanacSunGHA="179*52.1'"
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunGHA=Sun.GHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apySunGHA,angle.ToDecimal(navAlmanacSunGHA),0)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        localSunGHA=Sun.GHAAt(Y,M,D,h,m,s)        
        self.assertAlmostEqual(localSunGHA,angle.ToDecimal(navAlmanacSunGHA),2)
        Y,M,D,h,m,s=(2024,12,26,12,0,0) #and near 360*; astropy getting in count SD and HP of celestial body, so we also getting this into count
        navAlmanacSunGHA="359*48.4'"
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunGHA=Sun.GHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apySunGHA,angle.ToDecimal(navAlmanacSunGHA),0)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        localSunGHA=Sun.GHAAt(Y,M,D,h,m,s)        
        self.assertAlmostEqual(localSunGHA,angle.ToDecimal(navAlmanacSunGHA),2)

    #@unittest.skip("For debug pruposes")
    def test_CelestialObjectDecAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmanacDec="N 5*07.3'"
        almanac.source=0
        Venus=almanac.GetCelestialObject("Venus")
        apyVenusDec=Venus.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVenusDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Venus=almanac.GetCelestialObject("Venus")
        locVenusDec=Venus.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVenusDec,angle.ToDecimal(navAlmanacDec),2)
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacDec="S 15*52.8'"
        almanac.source=0
        Venus=almanac.GetCelestialObject("Venus")
        apyVenusDec=Venus.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVenusDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Venus=almanac.GetCelestialObject("Venus")
        locVenusDec=Venus.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVenusDec,angle.ToDecimal(navAlmanacDec),2)
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacDec="S 23*20.0'"
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        apySunDec=Sun.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apySunDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        locSunDec=Sun.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locSunDec,angle.ToDecimal(navAlmanacDec),2)
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacDec="-16*45.0'"
        almanac.source=0
        Sirius=almanac.GetCelestialObject("Sirius")
        apySiriusDec=Sirius.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apySiriusDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Sirius=almanac.GetCelestialObject("Sirius")
        locSiriusDec=Sirius.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locSiriusDec,angle.ToDecimal(navAlmanacDec),1) #for stars precision of my system is lower
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacDec="38*48.4'"
        almanac.source=0
        Vega=almanac.GetCelestialObject("Vega")
        apyVegaDec=Vega.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVegaDec,angle.ToDecimal(navAlmanacDec),0)
        almanac.source=1
        Vega=almanac.GetCelestialObject("Vega")
        locVegaDec=Vega.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVegaDec,angle.ToDecimal(navAlmanacDec),1) #for stars precision of my system is lower
    
    #@unittest.skip("For debug pruposes")
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
        self.assertAlmostEqual(locVegaSHA,angle.ToDecimal(navAlmanacSHA),1)
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacSHA="80*33.7'"
        almanac.source=0
        Vega=almanac.GetCelestialObject("Vega")
        apyVegaSHA=Vega.SHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVegaSHA,angle.ToDecimal(navAlmanacSHA),0)
        almanac.source=1
        Vega=almanac.GetCelestialObject("Vega")
        locVegaSHA=Vega.SHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVegaSHA,angle.ToDecimal(navAlmanacSHA),1)

    #@unittest.skip("For debug pruposes")
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

    #@unittest.skip("For debug pruposes")
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
