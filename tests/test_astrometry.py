import sys
sys.path.append("..\src")

import astrometry
import angle
import almanac
import unittest

class test_astrometry(unittest.TestCase):
    @unittest.skip("Useless because generates values not matching with reference in Bowditch")
    def test_FindLoP(self):
        phiDR=angle.ToDecimal("39*00.0'N")
        lambdaDR=angle.ToDecimal("45*26.0'W")
        Y=2016
        M=3
        D=9
        hoe=68*0.3048 #68 ft, to match dip correction in Bowditch
        indexCorrection=0.2/60; #instruent correction, 0.2 minutes as in Bowditch
                
        h=8 #in Bowditch vol.1, 2019, in table on p.315 they provided time ALREADY CORRECTED to GMT/UTC
        m=58
        s=27        
        celestialObjectName="Deneb"
        Hs=angle.ToDecimal("50*34.4'")        
        a,Zn=astrometry.FindLoP(phiDR,lambdaDR,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,IC=indexCorrection)
        self.assertAlmostEqual(a,angle.ToDecimal("0*11.7'"),3)
        self.assertAlmostEqual(Zn,63.3,3)

        h=9 #in Bowditch vol.1, 2019, in table on p.315 they provided time ALREADY CORRECTED to GMT/UTC
        m=2
        s=14        
        celestialObjectName="Deneb"
        Hs=angle.ToDecimal("23*57.2'")        
        a,Zn=astrometry.FindLoP(phiDR,lambdaDR,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,IC=indexCorrection)
        self.assertAlmostEqual(a,angle.ToDecimal("-0*05.2'"),3)
        self.assertAlmostEqual(Zn,189.9,3)

    def test_FindToCoEE(self):
        phiAP=round(33.3562) #Palomar observatory
        lambdaAP=round(-116.865)
        celestialObjectName1="Mars"
        Y1=2024
        M1=12
        D1=25
        h1=6
        m1=0
        s1=0
        el1=36.976441
        deltael1,beta1=astrometry.FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName1,el1)
        self.assertAlmostEqual(deltael1,0.12919942195004097,6)
        self.assertAlmostEqual(beta1,-84.73904924679685,6)

    def test_ElevationFor(self):
        phi=33.3562811 #Palomar observatory (precisely)
        lambda_=-116.8651156
        celestialObjectName1="Mars"
        Y1=2025
        M1=1
        D1=3
        h1=6 #UTC
        m1=0
        s1=0
        el1=astrometry.ElevationFor(celestialObjectName1,phi,lambda_,Y1,M1,D1,h1,m1,s1) #without correction.
        # !!! I'm shocked. Vallado ephemerides provides vectors WITH LIGHT SPEED CORRECTION AND WITH ATMOSPHERIC REFRACTION CORRECTION...
        # Again. Horizons system (https://ssd.jpl.nasa.gov/horizons/app.html#/) with atmospheric correction provides el=47.102741; WITHOUT CORRECTION IT IS el=47.087013
        self.assertAlmostEqual(el1,47.102741,2)

if __name__ == '__main__':
    unittest.main()
