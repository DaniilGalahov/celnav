import sys
sys.path.append("..\src")

import astrometry
import angle
import almanac
import unittest

class test_astrometry(unittest.TestCase):
    def test_ApplyElevationCorrectionTo(self):
        phiDR=angle.ToDecimal("39*00.0'N")
        lambdaDR=angle.ToDecimal("45*26.0'W")
        Y=2016
        M=3
        D=9        
        h=8 #in Bowditch vol.1, 2019, in table on p.315 they provided time ALREADY CORRECTED to GMT/UTC
        m=58
        s=27
        celestialObjectName="Deneb"
        Hs=angle.ToDecimal("50*34.4'")
        hoe=68*0.3048 #68 ft, to match dip correction in Bowditch
        indexCorrection=0.2/60; #instruent correction, 0.2 minutes as in Bowditch
        celestialObject = almanac.GetCelestialObject(celestialObjectName)
        horizontalParallax=celestialObject.HPAt(Y,M,D,h,m,s) #horizontal parallax of celestial object
        semiDiameter=celestialObject.SDAt(Y,M,D,h,m,s) #semi-diameter of celestial object
        Ho=astrometry.ApplyElevationCorrectionTo(Hs,hoe,HP=horizontalParallax,SD=semiDiameter,IC=indexCorrection)
        self.assertAlmostEqual(Ho,angle.ToDecimal("50*25.8'"),3)

    def test_FindLoP(self):
        phiDR=angle.ToDecimal("39*00.0'N")
        lambdaDR=angle.ToDecimal("45*26.0'W")
        Y=2016
        M=3
        D=9
        
        h=8 #in Bowditch vol.1, 2019, in table on p.315 they provided time ALREADY CORRECTED to GMT/UTC
        m=58
        s=27
        celestialObjectName="Deneb"
        Hs=angle.ToDecimal("50*34.4'")
        hoe=68*0.3048 #68 ft, to match dip correction in Bowditch
        indexCorrection=0.2/60; #0.2 minutes as in Bowditch
        a,Z=astrometry.FindLoP(phiDR,lambdaDR,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,IC=indexCorrection)
        print(angle.ToString(a))
        print(round(Z,3))

        h=9 #in Bowditch vol.1, 2019, in table on p.315 they provided time ALREADY CORRECTED to GMT/UTC
        m=2
        s=14
        celestialObjectName="Antares"
        Hs=angle.ToDecimal("23*57.2'")
        a,Z=astrometry.FindLoP(phiDR,lambdaDR,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,IC=indexCorrection)
        print(angle.ToString(a))
        print(round(Z,3))
        

if __name__ == '__main__':
    unittest.main()
