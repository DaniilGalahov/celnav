import setup

import ephemeris
import angle
import unittest

class test_ephemeris(unittest.TestCase):
    def test_ThetaGMSTAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST,angle.ToDecimal("245*40.4'"),2)

    def test_VectorToSunAt(self):
        vector_r=ephemeris.VectorToSunAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(vector_r[0],-123424888.55410339,6)
        self.assertAlmostEqual(vector_r[1],-76065442.2521582,6)
        self.assertAlmostEqual(vector_r[2],-32973519.977451567,6)

    def test_SunRADecAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        alpha,delta=ephemeris.SunRADecAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST-alpha,angle.ToDecimal("34*01.8'"),1)
        self.assertAlmostEqual(delta,angle.ToDecimal("12*48.8'S"),3)

    def test_VectorToMoonAt(self):
        vector_r=ephemeris.VectorToMoonAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(vector_r[0],350776.3186395564,6)
        self.assertAlmostEqual(vector_r[1],99750.93522518112,6)
        self.assertAlmostEqual(vector_r[2],38630.074790663246,6)    

    def test_MoonRADecAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        alpha,delta=ephemeris.MoonRADecAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST-alpha,angle.ToDecimal("229*45.9'"),1)
        self.assertAlmostEqual(delta,angle.ToDecimal("05*59.0'N")-angle.ToDecimal("0*02.9'S"),1)

    def test_VectorToPlanetAt(self):
        vector_r=ephemeris.VectorToPlanetAt("Mars",2023,10,27,14,0,0)
        self.assertAlmostEqual(vector_r[0],-289781490.3167944,6)
        self.assertAlmostEqual(vector_r[1],-227406332.329165,6)
        self.assertAlmostEqual(vector_r[2],-97854966.36474752,6)

    def test_PlanetRADecAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        alpha,delta=ephemeris.PlanetRADecAt("Mars",2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST-alpha,angle.ToDecimal("27*32.8'")+angle.ToDecimal("0*0.8'"),1)
        self.assertAlmostEqual(delta,angle.ToDecimal("14*52.8'S")-angle.ToDecimal("0*0.6'"),1)

if __name__ == '__main__':
    unittest.main()
