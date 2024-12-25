import sys
sys.path.append("..\src")

import astrometry
import angle
import timeprocessor
import unittest

class test_astrometry(unittest.TestCase):
    def test_CalculateIntercept(self):
        phigce=angle.ToDecimal("39*00.0'N")
        lambdae=angle.ToDecimal("45*26.0'W")
        timeZone=timeprocessor.TimeZone(lambdae)
        Y=2016
        M=3
        D=9
        h=8 #in Bowditch vol.1, 2019, in table on p.315 they provided time ALREADY CORRECTED to GMT/UTC
        m=58
        s=27
        celestialObjectName="Deneb"
        Hs=angle.ToDecimal("50*34.4'")
        hoe=68*0.3048 #68 ft, to match dip correction in Bowditch
        indexCorrection=0.2/60;
        a,Z=astrometry.CalculateIntercept(phigce,lambdae,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,IC=indexCorrection)
        print(angle.ToString(-a))
        print(round(Z,3))

if __name__ == '__main__':
    unittest.main()
