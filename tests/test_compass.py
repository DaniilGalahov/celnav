import setup

import compass
import unittest

class test_compass(unittest.TestCase):
    def test_COZCorrection(self):
        magHdg=0.0
        phi=51.1282921 #Baiterek, Astana
        lambda_=71.4305781
        Y=2025
        M=1
        D=17
        h=6 #UTC
        m=0
        s=0
        celestialObjectName="Sun"
        celestialObjectAz=149.0
        trueHdg,corr=compass.COZCorrection(magHdg,phi,lambda_,Y,M,D,h,m,s,celestialObjectName,celestialObjectAz)
        self.assertAlmostEqual(trueHdg,10.1,0)
        self.assertAlmostEqual(corr,10.1,0)

    def test_POZCorrection(self):
        magHdg=0.0
        phi0=51.1282921 #Baiterek, Astana
        lambda0=71.4305781
        phi1=51.0731459 #Grand Mosque
        lambda1=71.410925
        azObj=360.0-166.8
        trueHdg,corr=compass.POZCorrection(magHdg,phi0,lambda0,phi1,lambda1,azObj)
        self.assertAlmostEqual(trueHdg,10.1,-1)
        self.assertAlmostEqual(corr,10.1,-1)

if __name__ == '__main__':
    unittest.main()
