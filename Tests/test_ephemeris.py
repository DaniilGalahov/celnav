import sys
sys.path.append("..")

import ephemeris
import angle
import unittest

class test_ephemeris(unittest.TestCase):
    def test_CorrectedJulianDate(self):
        correctedJD=ephemeris.CorrectedJulianDate(2023,10,27,14,0,0)
        self.assertAlmostEqual(correctedJD,2460245.083733704,9)

    def test_ThetaGMSTAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST,angle.ToDecimal("245*40.4'"),2)

    def test_SunAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        alpha,delta,r=ephemeris.SunAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST-alpha,angle.ToDecimal("34*01.8'"),1)
        self.assertAlmostEqual(delta,angle.ToDecimal("12*48.8'S"),3)
        self.assertAlmostEqual(r,148683902.3907959,6)

    def test_MoonAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        alpha,delta,r=ephemeris.MoonAt(2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST-alpha,angle.ToDecimal("229*45.9'"),1)
        self.assertAlmostEqual(delta,angle.ToDecimal("05*59.0'N")-angle.ToDecimal("0*02.9'S"),1)
        self.assertAlmostEqual(r,366723.3630300349,6)

    def test_PlanetAt(self):
        thetaGMST=ephemeris.ThetaGMSTAt(2023,10,27,14,0,0)
        alpha,delta,r=ephemeris.PlanetAt("Mars",2023,10,27,14,0,0)
        self.assertAlmostEqual(thetaGMST-alpha,angle.ToDecimal("27*32.8'")+angle.ToDecimal("0*0.8'"),1)
        self.assertAlmostEqual(delta,angle.ToDecimal("14*52.8'S")-angle.ToDecimal("0*0.6'"),1)
        self.assertAlmostEqual(r,381133329.4647586,6)

if __name__ == '__main__':
    unittest.main()
