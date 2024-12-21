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
        h=8+timeZone
        m=58 #?? 45
        s=27
        #Y,M,D,h,m,s=timeprocessor.GMTtoUTC(Y,M,D,h,m,s,lambdae)
        celestialObjectName="Deneb"
        Hs=angle.ToDecimal("50*34.4'")
        aoe=68*0.3048 #68 ft, to match dip correction in Bowditch
        indexCorrection=0.2/60;
        a,Z=astrometry.CalculateIntercept(phigce,lambdae,Y,M,D,h,m,s,celestialObjectName,Hs,aoe,IC=indexCorrection)
        #print(angle.ToString(a))
        #print(angle.ToString(Z))
        

if __name__ == '__main__':
    unittest.main()
