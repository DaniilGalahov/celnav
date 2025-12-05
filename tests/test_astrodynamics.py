import setup

import external.astrodynamics.algorithms as algorithms
from external.astrodynamics.frames import IJK
from external.astrodynamics.external.math import *
import unittest

class test_astrodynamics(unittest.TestCase):
    def test_ConvTime(self):
        #print("\n"+"ConvTime(2004,5,14,HMSToTime(16,43,00),-0.463326,32.0)")
        UT1,TAI,GPS,TT,TDB,TCB,TCG,TUT1,TTT,TTDB=algorithms.ConvTime(2004,5,14,algorithms.HMSToTime(16,43,00),-0.463326,32.0)
        self.assertAlmostEqual(UT1,60179.536674,6)
        self.assertAlmostEqual(TAI,60212.0,6)
        self.assertAlmostEqual(GPS,60193.0,6)
        self.assertAlmostEqual(TT,60244.184,6)
        self.assertAlmostEqual(TDB,60244.1852407941,6)
        self.assertAlmostEqual(TCB,60257.57472614667,6)
        self.assertAlmostEqual(TCG, 60244.78588758058,6)
        self.assertAlmostEqual(TUT1,0.04367410054524709,6)
        self.assertAlmostEqual(TTT,0.04367412103074848,6)
        self.assertAlmostEqual(TTDB,0.0436741210311437,6)

    def test_JulianDate(self):
        #print("\n"+"JulianDate(1996,10,26,14,20,00)")
        JD=algorithms.JulianDate(1996,10,26,14,20,00)
        #print(JD)
        self.assertAlmostEqual(JD,2450383.097222,6)

    def test_JDtoGregorianDate(self):
        #print("\n"+"JDtoGregorianDate(2449877.3458762)")
        Year,Mon,Day,h,min_,s=algorithms.JDtoGregorianDate(2449877.3458762)
        #print(Year,Mon,Day,h,min_,s)
        self.assertEqual(Year,1995)
        self.assertEqual(Mon,6)
        self.assertEqual(Day,8)
        self.assertEqual(h,20)
        self.assertEqual(min_,18)
        self.assertAlmostEqual(s,3.703690,5)

    def test_LSTime(self):
        #print("\n"+"LSTime(JulianDate(1992,8,20,12,14,00),0,-104)")
        ThetaLST,ThetaGMST=algorithms.LSTime(algorithms.JulianDate(1992,8,20,12,14,00),0,-104) #for precise applications we must calculate UT1 first (Eq.3-49 in Vallado)
        #print(ThetaLST,ThetaGMST)
        self.assertAlmostEqual(ThetaLST,48.578788,6)
        self.assertAlmostEqual(ThetaGMST,152.578788,6)

    def test_HMSToTime(self):
        #print("\n"+"HMSToTime(13,22,45.98)")
        tau=algorithms.HMSToTime(13,22,45.98)
        #print(tau)
        self.assertAlmostEqual(tau,48165.98,2)

    def test_TimeToHMS(self):
        #print("\n"+"TimeToHMS(48165.98)")
        h,min_,s=algorithms.TimeToHMS(48165.98)
        #print(h,min_,s)
        self.assertEqual(h,13)
        self.assertEqual(min_,22)
        self.assertAlmostEqual(s,45.98,6)

    def test_DayOfYearToYMD(self):
        #print("\n"+"DayOfYearToYMD(1992, 129):")
        y,m,d=algorithms.DayOfYearToYMD(1992, 129)
        #print(y,m,d)
        self.assertEqual(y,1992)
        self.assertEqual(m,5)
        self.assertEqual(d,8)
        #print("\n"+"DayOfYearToYMD(2024, 1):")
        y,m,d=algorithms.DayOfYearToYMD(2024, 1)
        #print(y,m,d)
        self.assertEqual(y,2024)
        self.assertEqual(m,1)
        self.assertEqual(d,1)
        #print("\n"+"DayOfYearToYMD(2024, 366):")
        y,m,d=algorithms.DayOfYearToYMD(2024, 366)
        #print(y,m,d)
        self.assertEqual(y,2024)
        self.assertEqual(m,12)
        self.assertEqual(d,31)

    def test_KepEqtnE(self):
        #print("\n"+"KepEqtnE(235.4,0.4):")
        E=algorithms.KepEqtnE(235.4,0.4)
        #print(E)
        self.assertAlmostEqual(E, 220.512074, 5)

    def test_Anomalytonu(self):
        #print("\n"+"Anomalytonu(0.5,59.999999, None, None, None, None):")
        nuE=algorithms.Anomalytonu(0.5,59.999999, None, None, None, None)
        #print("nu ecc="+str(nuE))
        #print("Anomalytonu(1.0, None, 0.999999, 25512, 25512, None):") #At true anomaly = 90 deg. on parabolic orbit, r=p.
        nuP=algorithms.Anomalytonu(1.0, None, 0.999999, 25512, 25512, None)
        #print("nu par="+str(nuP))
        #print("Anomalytonu(1.5, None, None, None, None, 0.962423):")
        nuH=algorithms.Anomalytonu(1.5, None, None, None, None, 0.962423)
        #print("nu hyp="+str(nuH))
        self.assertAlmostEqual(nuE,90,5)
        self.assertAlmostEqual(nuP,90,5)
        self.assertAlmostEqual(nuP,90,5)

    def test_COE2RV(self):
        #print("\n"+"COE2RV(11067.799503,0.832853,87.869126,227.898260,53.384937,92.335149,145.720087,55.282707,247.806452)")
        vector_rIJK,vector_vIJK=algorithms.COE2RV(11067.799503,0.832853,87.869126,227.898260,53.384937,92.335149,145.720087,55.282707,247.806452)
        #print("Vector r IJK:")
        #print(vector_rIJK)
        #print("Vector v IJK:")
        #print(vector_vIJK)
        self.assertTrue(magnitude(vector_rIJK - vector([6524.834,6862.875,6448.296]))<1)
        self.assertTrue(magnitude(vector_vIJK - vector([4.901327,5.533756,-1.976341]))<1)

    def test_GeocentricRadec(self):
        #print("\n"+"GeocentricRadec(vector_rIJK,vector_vIJK)")
        vector_rECI=vector([1752246215.0,-3759563433.0,-1577568105.0])
        vector_vECI=vector([-18.323,18.332,7.777])
        r,alpha,delta,rdot,alphadot,deltadot=algorithms.GeocentricRadec(vector_rECI,vector_vECI)
        #print(r,alpha,delta,rdot,alphadot,deltadot)
        self.assertAlmostEqual(r,4437725220.272867,6)
        self.assertAlmostEqual(alpha,294.98914582892905,9)
        self.assertAlmostEqual(delta,-20.823494443069105,9)
        self.assertAlmostEqual(rdot,-25.53007808735388,6)
        self.assertAlmostEqual(alphadot,-1.2243406550048548e-07,9)
        self.assertAlmostEqual(deltadot,-1.793932810519285e-08,9)

    def test_Sun(self):
        #print("\n"+"Sun()")
        JDUT1=algorithms.JulianDate(2006,4,2,0,0,0)
        vector_rSun=algorithms.Sun(JDUT1)
        #print(vector_rSun)
        self.assertAlmostEqual(vector_rSun[IJK.axis.I],1.46186237e+08,0)
        self.assertAlmostEqual(vector_rSun[IJK.axis.J],2.8789137e+07,0)
        self.assertAlmostEqual(vector_rSun[IJK.axis.K],1.2481133e+07,0)

    def test_Moon(self):
        #print("\n"+"Moon()")
        JDUT1=algorithms.JulianDate(1994,4,28,0,0,0)
        vector_rMoon=algorithms.Moon(JDUT1)
        #print(vector_rMoon)
        self.assertAlmostEqual(vector_rMoon[IJK.axis.I],-134252.52460012,3)
        self.assertAlmostEqual(vector_rMoon[IJK.axis.J],-310924.48030485,3)
        self.assertAlmostEqual(vector_rMoon[IJK.axis.K],-128261.23269325,3)

    def test_PlanetRV(self):
        #print("\n"+"PlanetRV()")
        JD=algorithms.JulianDate(1994,5,20,20,0,0)
        vector_rXYZFK5,vector_vXYZFK5=algorithms.PlanetRV("Jupiter",JD)
        #print(vector_rXYZFK5,vector_vXYZFK5)
        self.assertAlmostEqual(vector_rXYZFK5[IJK.axis.I],-6.10482809e+08,0)
        self.assertAlmostEqual(vector_rXYZFK5[IJK.axis.J],-4.96674731e+08,0)
        self.assertAlmostEqual(vector_rXYZFK5[IJK.axis.K],-1.98055267e+08,0)
        self.assertAlmostEqual(vector_vXYZFK5[IJK.axis.I],8.45298597,3)
        self.assertAlmostEqual(vector_vXYZFK5[IJK.axis.J],-8.40204081,3)
        self.assertAlmostEqual(vector_vXYZFK5[IJK.axis.K],-3.80773764,3)

    def test_Site(self):
        #print("\n"+"Site(60,0.01,0.4684027380039782)") #params of SPb, ~00:30 19.10.2021
        vector_rIJK,vector_vIJK=algorithms.Site(60,0.01,0.4684027380039782)
        #print(vector_rIJK,vector_vIJK)
        #print(magnitude(vector_rIJK),magnitude(vector_vIJK)) # correct values must be smaller than Rearth (we are to the north of equatorial bulge) and slower than equatorial rotation speed (equatorial is 460 m/s, and our must be 460*cos(60), i.e., about 230)
        self.assertAlmostEqual(vector_rIJK[IJK.axis.I],3197.0027567,3)
        self.assertAlmostEqual(vector_rIJK[IJK.axis.J],26.13662331,3)
        self.assertAlmostEqual(vector_rIJK[IJK.axis.K],5500.48577684,3)
        self.assertAlmostEqual(vector_vIJK[IJK.axis.I],-0.00190591,6)
        self.assertAlmostEqual(vector_vIJK[IJK.axis.J],0.23312914,6)
        self.assertAlmostEqual(vector_vIJK[IJK.axis.K],0,6)
        # addition from 27.02.2024 - algorithm returning vectors in IJK (i.e., in non-rotating Earth-centered system. Rotation of position vector achieved by applying correct LST for algorithm.)
        # To calculate LST, we may use local time, but for compatibility we should use GMT.
        Y=2024
        M=2
        D=27
        h=10
        m=40
        s=00
        #JD is 10:40 AM 27/10/2024
        JD=algorithms.JulianDate(Y,M,D,h,m,s)
        phigd=60.0
        lambda_=30.0
        #position is St.Petersburg, Lisiy Nos
        thetaLST,thetaGMST=algorithms.LSTime(JD,0.0,lambda_)
        vector_rIJK,vector_vIJK=algorithms.Site(phigd,0,thetaLST)
        #print(vector_rIJK,vector_vIJK)
        #print(magnitude(vector_rIJK),magnitude(vector_vIJK))
        self.assertAlmostEqual(vector_rIJK[IJK.axis.I],3112.28403951,3)
        self.assertAlmostEqual(vector_rIJK[IJK.axis.J],-731.55029612,3)
        self.assertAlmostEqual(vector_rIJK[IJK.axis.K],5500.47711658,3)
        self.assertAlmostEqual(vector_vIJK[IJK.axis.I],0.0533455,6)
        self.assertAlmostEqual(vector_vIJK[IJK.axis.J],0.22695136,6)
        self.assertAlmostEqual(vector_vIJK[IJK.axis.K],0,6)

def test_IJKtoLATLON(self):
        #print("\n"+"IJKtoLATLON(vector_r,thetaGMST)")
        vector_r=vector([2057.757505244139, 4942.510062874035, 3455.0627789492773])
        thetaGMST=184.24603021840255
        phigc,phigd,lambda_,hellip=utility.IJKtoLATLON(vector_r,thetaGMST)
        #print(phigc,phigd,lambda_,hellip)
        self.assertAlmostEqual(phigc,32.83626790629223,6)
        self.assertAlmostEqual(phigd,33.01184821755222,6)
        self.assertAlmostEqual(lambda_,-116.84987494034617,6)
        self.assertAlmostEqual(hellip,0.00402169704921107,6)

if __name__ == '__main__':
    unittest.main()
