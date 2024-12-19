import sys
sys.path.append("..\src")

import astrometry
import angle
import unittest

class test_astrometry(unittest.TestCase):
    def test_CalculateIntercept(self):
        phigce=angle.ToDecimal("14*45'N")
        lambdae=angle.ToDecimal("30*00'W")
        Y=1974
        M=9
        D=9
        h=21 #local 19
        m=20
        s=3
        celestialObjectName="Arcturus"
        deltats=angle.ToDecimal("28*29.5'")
        hoh=31*0.3048
        T=15.0
        P=1013.25        
        p,z=astrometry.CalculateIntercept(phigce,lambdae,Y,M,D,h,m,s,celestialObjectName,deltats,hoh,T,P)
        print(p,z)
        

if __name__ == '__main__':
    unittest.main()
