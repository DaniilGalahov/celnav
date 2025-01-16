import sys
sys.path.append("..\src")

import astrometry
import position
import unittest

class test_position(unittest.TestCase):
    def test_FromToCoEEo2CO(self):
        phi0=33.3562811 #Palomar observatory (precisely)
        lambda0=-116.8651156
        phiAP=round(phi0)
        lambdaAP=round(lambda0)
        celestialObjectName="Sun"
        Y1=2024
        M1=12
        D1=25
        h1=18
        m1=0
        s1=0
        Hs1=27.766345
        Hs1+=astrometry.ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)
        Y2=2024
        M2=12
        D2=25
        h2=19
        m2=0
        s2=0
        Hs2=32.172951
        Hs2+=astrometry.ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)
        deltael1,beta1=astrometry.FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
        deltael2,beta2=astrometry.FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
        phi,lambda_=position.FromToCoEEo2CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2)
        self.assertAlmostEqual(phi,phi0,2)
        self.assertAlmostEqual(lambda_,lambda0,1)

    def test_FromToCoEEo3CO(self):
        phi0=33.3562811 #Palomar observatory (precisely)
        lambda0=-116.8651156
        phiAP=round(phi0)
        lambdaAP=round(lambda0)
        celestialObjectName="Sun"
        Y1=2024
        M1=12
        D1=25
        h1=18
        m1=0
        s1=0
        Hs1=27.766345
        Hs1+=astrometry.ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)
        Y2=2024
        M2=12
        D2=25
        h2=19
        m2=0
        s2=0
        Hs2=32.172951
        Hs2+=astrometry.ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)
        Y3=2024
        M3=12
        D3=25
        h3=20
        m3=0
        s3=0
        Hs3=33.235187
        Hs3+=astrometry.ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)
        deltael1,beta1=astrometry.FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
        deltael2,beta2=astrometry.FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
        deltael3,beta3=astrometry.FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
        phi,lambda_=position.FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
        self.assertAlmostEqual(phi,phi0,2)
        self.assertAlmostEqual(lambda_,lambda0,1)

if __name__ == '__main__':
    unittest.main()
