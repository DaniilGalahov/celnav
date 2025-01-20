import sys
sys.path.append("..\src")

import almanac
import angle
import unittest

class test_almanac(unittest.TestCase):
    #@unittest.skip("For debug pruposes")
    def test_VectorAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        almanac.source=0
        Sun=almanac.GetCelestialObject("Sun")
        vector_r=Sun.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],-123422491.4841269,0) #matching local almanac within 50000 km
        self.assertAlmostEqual(vector_r[1],-76064194.63567881,0)
        self.assertAlmostEqual(vector_r[2],-32974456.4210693,0)
        Moon=almanac.GetCelestialObject("Moon")
        vector_r=Moon.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],350305.5150144167,0) #about 150 km difference
        self.assertAlmostEqual(vector_r[1],99859.0066481714,0) #1700 km diff
        self.assertAlmostEqual(vector_r[2],38177.40379207954,0) #1200 km diff
        Mars=almanac.GetCelestialObject("Mars")
        vector_r=Mars.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],-289745293.9645509,0) #more than 1M km diff
        self.assertAlmostEqual(vector_r[1],-227409116.4498696,0)
        self.assertAlmostEqual(vector_r[2],-97864403.20811118,0)
        Vega=almanac.GetCelestialObject("Vega")
        vector_r=Vega.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],1433256483553.1458,2)
        self.assertAlmostEqual(vector_r[1],-8625136168509.275,2)
        self.assertAlmostEqual(vector_r[2],7031188970624.335,2)
        almanac.source=1
        Sun=almanac.GetCelestialObject("Sun")
        vector_r=Sun.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],-123424888.55410339,6)
        self.assertAlmostEqual(vector_r[1],-76065442.2521582,6)
        self.assertAlmostEqual(vector_r[2],-32973519.977451567,6)
        Moon=almanac.GetCelestialObject("Moon")
        vector_r=Moon.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],350776.3186395564,6)
        self.assertAlmostEqual(vector_r[1],99750.93522518112,6)
        self.assertAlmostEqual(vector_r[2],38630.074790663246,6)
        Mars=almanac.GetCelestialObject("Mars")
        vector_r=Mars.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],-289781490.3167944,6)
        self.assertAlmostEqual(vector_r[1],-227406332.329165,6)
        self.assertAlmostEqual(vector_r[2],-97854966.36474752,6)
        Vega=almanac.GetCelestialObject("Vega")
        vector_r=Vega.VectorAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(vector_r[0],1433125494782.9514,2)
        self.assertAlmostEqual(vector_r[1],-8625195086140.118,2)
        self.assertAlmostEqual(vector_r[2],7031143396050.94,2)

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
        self.assertAlmostEqual(apySiriusDec,angle.ToDecimal(navAlmanacDec),1) #increased precision of star positions with astropy
        almanac.source=1
        Sirius=almanac.GetCelestialObject("Sirius")
        locSiriusDec=Sirius.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locSiriusDec,angle.ToDecimal(navAlmanacDec),2) #reached higher precession for stars for my almanac with counting precession and nutation
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacDec="38*48.4'"
        almanac.source=0
        Vega=almanac.GetCelestialObject("Vega")
        apyVegaDec=Vega.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVegaDec,angle.ToDecimal(navAlmanacDec),1)
        almanac.source=1
        Vega=almanac.GetCelestialObject("Vega")
        locVegaDec=Vega.DecAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVegaDec,angle.ToDecimal(navAlmanacDec),2)
    
    #@unittest.skip("For debug pruposes")
    def test_CelestialObjectSHAAt(self):
        Y,M,D,h,m,s=(2023,10,27,14,0,0)
        navAlmanacSHA="80*34.1'" #in N.A. 80*34.1'
        almanac.source=0
        Vega=almanac.GetCelestialObject("Vega")
        apyVegaSHA=Vega.SHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(apyVegaSHA,angle.ToDecimal(navAlmanacSHA),0)
        almanac.source=1
        Vega=almanac.GetCelestialObject("Vega")
        locVegaSHA=Vega.SHAAt(Y,M,D,h,m,s)
        self.assertAlmostEqual(locVegaSHA,angle.ToDecimal(navAlmanacSHA),1)  #my almanac isn't precise with stars. Can not understand the reason.
        Y,M,D,h,m,s=(2024,12,26,14,0,0)
        navAlmanacSHA="80*33.7'" #in N.A. 80*33.7'
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
