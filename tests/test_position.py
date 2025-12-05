import setup

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

    def test_FromP3A3(self):
        phi0=51.1282921 #Baiterek, Astana
        lambda0=71.4305781
        phi1=51.0731459 #Grand Mosque
        lambda1=71.410925
        phi2=51.1256397 #Harzat Sultan Mosque
        lambda2=71.4724698
        phi3=51.1090188 #Barys Arena
        lambda3=71.3953671
        alpha12=96.6
        alpha23=144+83.4
        alpha31=36
        phi,lambda_=position.FromP3A3(phi1,lambda1,phi2,lambda2,phi3,lambda3,alpha12,alpha23,alpha31)
        self.assertAlmostEqual(phi,phi0,1)
        self.assertAlmostEqual(lambda_,lambda0,1) #726 m deviation, almost same as FromP3R3

    def test_FromP3R3(self):
        phi0=51.1282921 #Baiterek, Astana
        lambda0=71.4305781
        phi1=51.0731459 #Grand Mosque
        lambda1=71.410925
        phi2=51.1256397 #Harzat Sultan Mosque
        lambda2=71.4724698
        phi3=51.1090188 #Barys Arena
        lambda3=71.3953671
        r1=6.31 #km
        r2=2.97
        r3=3.25
        phi,lambda_=position.FromP3R3(phi1,lambda1,phi2,lambda2,phi3,lambda3,r1,r2,r3)
        self.assertAlmostEqual(phi,phi0,1)
        self.assertAlmostEqual(lambda_,lambda0,1) #865 m deviation, almost same as FromP3Z3

if __name__ == '__main__':
    unittest.main()
