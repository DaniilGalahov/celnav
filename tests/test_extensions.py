import setup

from math import cos, degrees
from numpy import array as vector
from numpy.linalg import norm as mag

import celnav
import extensions
import unittest

class test_extensions(unittest.TestCase):
    def test_SightReductionCC(self):
        phiAP=round(33.3562811) #Palomar observatory (precisely)
        lambdaAP=round(-116.8651156)
        celestialObjectName1="Mars"
        Y1=2024
        M1=12
        D1=25
        h1=6
        m1=0
        s1=0
        el1=36.976441
        a1,Z1=extensions.SightReductionCC(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName1,el1)
        self.assertAlmostEqual(a1,0.12967432104721865,6)
        self.assertAlmostEqual(Z1,-84.7389551487631,6)
        a1,Z1=extensions.SightReductionCC(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName1,el1,False)
        self.assertAlmostEqual(a1,0.14870698327781895,6)
        self.assertAlmostEqual(Z1,-84.7389551487631,6)

    def test_DriftCorrection(self):
        def SunSightReductionViaLT(phiDR,lambdaDR,Yl,Ml,Dl,hl,ml,sl,el):
            #converting time to GMT
            Y,M,D,h,m,s=celnav.LTToGMT(Yl,Ml,Dl,hl,ml,sl,lambdaDR)

            #preparing sight reduction
            celestialObjectName="Sun"
            T=32.0    #environment temperature, degrees Celsius
            P=1013.25 #environment pressure, millibars

            #do sight reduction
            a,Z=celnav.SightReduction(phiDR, lambdaDR,
                                      Y, M, D, h, m, s,
                                      celestialObjectName, el,
                                      T=T, P=P)
            return a, Z
        
        #dead reckoning
        phiDR=0.0 #latitude, decimal degrees
        lambdaDR=0.0 #longitude, decimal degrees
        
        z=90.0 #straight E
        v=60.0 #kts

        #Sight1, at position [0;0]
        Y1=2026
        M1=3
        D1=5
        h1=14
        m1=0
        s1=0
        el1=62.275364

        #Sight 2, at position [0;0.25]
        Y2=2026
        M2=3
        D2=5
        h2=14
        m2=15
        s2=0
        el2=58.364564

        #Calculating sight reductions
        a1,Z1 = SunSightReductionViaLT(phiDR,lambdaDR,Y1,M1,D1,h1,m1,s1,el1)
        a2,Z2 = SunSightReductionViaLT(phiDR,lambdaDR,Y2,M2,D2,h2,m2,s2,el2)
        #print("a1:",a1)

        a1=extensions.DriftCorrection(Y1,M1,D1,h1,m1,s1,
                                      a1,Z1,
                                      Y2,M2,D2,h2,m2,s2,
                                      z,v)

        #Estimating geographical position
        phi,lambda_=celnav.TwoObjectFix(phiDR,lambdaDR,a1,Z1,a2,Z2)
        print("Calculated position lat/lon [dd]:",round(phi,3),round(lambda_,3))

        vector_pactual=vector([0.0,0.25])
        vector_pfix=vector([phi,lambda_])
        d=mag(vector_pfix-vector_pactual)*60.0*1.852
        print("Deviation [km]:",round(d,1))
        self.assertTrue(d<1.0)


        #==============================================================

        #Althernative Sight 2, at position [0;-0.25]
        Y2=2026
        M2=3
        D2=5
        h2=14
        m2=15
        s2=0
        el2=58.854539

        #Calculating sight reductions
        a1,Z1 = SunSightReductionViaLT(phiDR,lambdaDR,Y1,M1,D1,h1,m1,s1,el1)
        a2,Z2 = SunSightReductionViaLT(phiDR,lambdaDR,Y2,M2,D2,h2,m2,s2,el2)
        #print("a1:",a1)

        a1=extensions.DriftCorrection(Y1,M1,D1,h1,m1,s1,
                                      a1,Z1,
                                      Y2,M2,D2,h2,m2,s2,
                                      z,v)

        #Estimating geographical position
        phi,lambda_=celnav.TwoObjectFix(phiDR,lambdaDR,a1,Z1,a2,Z2)
        print("Calculated position lat/lon [dd]:",round(phi,3),round(lambda_,3))

        vector_pactual=vector([0.0,-0.25])
        vector_pfix=vector([phi,lambda_])
        d=mag(vector_pfix-vector_pactual)*60.0*1.852
        print("Deviation [km]:",round(d,1))
        self.assertTrue(d<1.0)

if __name__ == '__main__':
    unittest.main()
