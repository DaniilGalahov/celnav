import sys
sys.path.append("..\src")

import astrometry
import angle
import almanac
import unittest

class test_astrometry(unittest.TestCase):
    def test_AzElFor(self):
        '''
        So. Before I start the testing, I need to record all my previous way of acting to prevent mistakes.
        
        30.12.2024 I found out that Horizons system (https://ssd.jpl.nasa.gov/horizons/app.html#/) with atmospheric correction provides el=47.102741, and WITHOUT CORRECTION el=47.087013. My almanac
        output was 47.10182375676978. Difference of almanac value with Horizons corrected el was d=0.000917, with Horizons uncorrected - 0.014811; i.e., 16.151581 TIMES!!!
        I started to think that Vallado's ephemerides providing values with already applied refraction correction.

        After I met this strange bug, my initial suggestion was that Vallado's ephemerides provides value ALREADY WITH refraction correction.
        
        I continue the work. When I finished position fix procedures, I found out that results are not so correct (precision was about 1 mile).

        To fix this, I added intuitive (and scientifically improper) corrections (rotations of vector to planet) to coloc.py (for planets, to minimize deviation of fixed geographical point on Earth).
        After adding this corrections, I found out that now "raw" values of azimuth and elevation (without refraction) from my almanac matching "raw" values of azimuth and elevation (without refraction)
        from Horizons system.

        I thought that this corrections was required because of way how scientists in JPL measured positions of planets (it looked like they measured them not from visual center of planet,
        but from a corner of a photo of a planet). But I could not explain exact values of coefficients I used to fix this error.

        I added correction of precession and nutation. This reduced size of error, but the trouble did not get away.

        I thought that the root of trouble is in a way of photografical measuring of position of planets is only my suggestion. I think I need to test the size of differences between azimuths and elevations
        of a planets calculated by my almanac, and azimuths and elevations recieved from Horizons. This could possibly help me to find a source of an error.

        Now it's 11.01.2025, and I am starting testing.
        '''
            
        phi=33.3562811 #Palomar observatory (precisely)
        lambda_=-116.8651156

        #basic tests
        celestialObjectName="Betelgeuse" #by NAOJ, az: 151.8944, el: 61.4543 w. refraction, 61.3328 w/o. refraction
        Y=2025
        M=1
        D=3
        h=5 #UTC
        m=58
        s=51
        az,el=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.
        self.assertAlmostEqual(az,151.8944,1) #azimuth precision for stars is average
        self.assertAlmostEqual(el,61.3328,2) #Matched.

        celestialObjectName="Sun" #By Horizons; using precise coordinates mentioned here (not those which are pre-defined in Horizons)
        Y=2025
        M=1
        D=3
        h=17 #UTC
        m=0
        s=0
        az,el=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(az,137.775247,2) #Matched.
        self.assertAlmostEqual(el,20.509091,1) #not matched at 2 decimals

        celestialObjectName="Venus"
        Y=2025
        M=1
        D=3
        h=20 #UTC
        m=0
        s=0
        az,el=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(az,127.807802,2) #Matched!!!
        self.assertAlmostEqual(el,26.439441,1) #not matched at 2 decimals

        celestialObjectName="Mars"
        Y=2025
        M=1
        D=3
        h=6 #UTC
        m=0
        s=0
        az,el=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(az,89.925673,1) #not matched at 2 decimals
        self.assertAlmostEqual(el,47.084832,1) #not matched at 2 decimals

        celestialObjectName="Jupiter"
        Y=2025
        M=1
        D=3
        h=4 #UTC
        m=0
        s=0
        az,el=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(az,110.744685,1) #not matched at 2 decimals
        self.assertAlmostEqual(el,64.717721,2) #Matched!!!

        celestialObjectName="Saturn"
        Y=2025
        M=1
        D=3
        h=3 #UTC
        m=0
        s=0
        az,el=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(az,234.070866,1) #not matched at 2 decimals
        self.assertAlmostEqual(el,31.028380,1) #not matched at 2 decimals

        '''
        Initial testing done.

        After this, I made special "full-scale" deviation testing, to test deviation in 30 years. Code of this tests is moved from here to "astrometry/devtest.py"

        So, basing on deep testing, I understood that Vallado's ephemerides providing "true" position of a planet (without any refraction correction)

        But they do it non-precisely.

        Deviation of azimuth and elevation are systematic but very complex, and I can not describe them mathematically.

        I think that I should stop my tries of achieve high precision for now. I should finish all other parts of system, i.e., geodesy,
        great circle navigation and star compass. After this, I should preform a complex test of precision for multiple positions on Earth,
        to understand real precision of my algorithms.

        12.01.2025
        Complex test of precision finished. Average deviation of position determination is about 500 m. Not bad, but how to reduce this?

        13.01.2025
        Found out article, describing generation of MOS - Mean Orbit Solutions. MOS are the way how Vallado described orbits of planets.
        This way is not too precise by definition - it's MEAN orbit solutions. For Mars and Saturn deviations can match 60" and 600" respectably.

        There is a way to fix this. J.L.Simon in his article "Numerical expressions for
        precession formulae and mean elements for the Moon and the planets" described a way
        to generate corrections for achieve higher precision. But this is pretty complex code,
        so I will implement it later.
        '''
        
    #@unittest.skip("For debug purposes")
    def test_ElevationCorrection(self):
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
        Hc=astrometry.ElevationCorrection(celestialObjectName,Y,M,D,h,m,s,Hs,indexCorrection,hoe)
        Ho=angle.ToDecimal("50*25.8'")
        self.assertAlmostEqual(Hc,Ho-Hs,3)

    #@unittest.skip("For debug purposes")
    def test_FindToCoEE(self):
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
        el1=el1+astrometry.ElevationCorrection(celestialObjectName1,Y1,M1,D1,h1,m1,s1,el1)
        deltael1,beta1=astrometry.FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName1,el1)
        self.assertAlmostEqual(deltael1,0.12967432104721865,6)
        self.assertAlmostEqual(beta1,-84.7389551487631,6)

if __name__ == '__main__':
    unittest.main()
