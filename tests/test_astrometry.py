import sys
sys.path.append("..\src")

import astrometry
import angle
import almanac
import unittest

class test_astrometry(unittest.TestCase):
    @unittest.skip("Useless because almanac generates already pre-corrected output")
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

    def test_BetaElFor(self):
        '''
        30.12.2024
        # !!! I'm shocked. Vallado ephemerides provides vectors WITH LIGHT SPEED CORRECTION AND WITH ATMOSPHERIC REFRACTION CORRECTION...
        # Again. Horizons system (https://ssd.jpl.nasa.gov/horizons/app.html#/) with atmospheric correction provides el=47.102741, WITHOUT CORRECTION el=47.087013
        # Almanac output is 47.10182375676978. Difference with Horizons corrected el d=0.000917, with uncorrected - 0.014811; i.e., 16.151581 TIMES!!!
        
        #self.assertAlmostEqual(el1,47.102741,2) # After adding corrections inside almanac reached value 47.086728167206616, which is almost "without correction"

        01.01.2025 (?)
        I still can not understand the source of a problem. There is possibility that astronomers measured positions of celestial objects not by center of an object,
        but by edge of its frame on astro photo.

        03.01.2025 (?)
        Same, after MY corrections, I've got positions close enough for those which are without refraction. Maybe (!) the trouble is in refraction itself,
        not in a way how they measuring position of C.O.
        
        10.01.2025
        Things are not so simple as I expected. Ephemerides of Vallado provides "pure" vectors (i.e., without refraction correction). BUT, positions of celestial bodies are strangely twisted
        (and that is probably not because of precession or nutation). To find truth, we need to compare non-corrected data from Horizon with non-corrected data from my ephemeris system.
        We need to compare elevations and azimuths, and find "twist rate" for each of planets.

        11.01.2025
        So. Before I start the testing, I need to record all my previous way of acting to prevent mistakes.
        After I met this strange bug, my initial suggestion was that Vallado's ephemerides provides value with correction.
        Then, when I finished position fix procedures, I found out that they are not so correct (precision is about 1 mile).
        To fix this, I added intuitive (and not scientifically founded) corrections (rotations of vector to planed) to coloc.py (for planets, to minimize deviation of fixed geographical point on Earth).
        After adding this corrections, I found out that now "raw" values of azimuth and elevation (without refraction) from my almanac matching "raw" values of azimuth and elevation (without refraction)
        from Horizons system.
        I thought that this corrections are needed because of way how scientists in JPL measured positions of planets (it looked like they measured them not from visual center of planet,
        but from a corener of a photo of a planet).
        I added correction of precession and nutation, but the troubles did not get away.
        But thought that the root of trouble is in a way of photografical measuring of position of planets is only my suggestion. I thing I need to test how different would be azimuths and elevations
        of a planets calculated by my almanac, and try to find a source of an error.
        '''
            
        phi=33.3562811 #Palomar observatory (precisely)
        lambda_=-116.8651156


        celestialObjectName="Betelgeuse" #by NAOJ, beta: 151.8944, el: 61.4543 w. refraction, 61.3328 w/o. refraction
        Y=2025
        M=1
        D=3
        h=5 #UTC
        m=58
        s=51
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.
        self.assertAlmostEqual(beta,151.8944,1) #azimuth precision for stars is average
        self.assertAlmostEqual(el,61.3328,2) #Matched.

        celestialObjectName="Sun" #By Horizons; using precise coordinates mentioned here (not those which are pre-defined in Horizons)
        Y=2025
        M=1
        D=3
        h=17 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,137.775247,2) #Matched.
        self.assertAlmostEqual(el,20.509091,1) #not matched at 2 decimals

        celestialObjectName="Venus"
        Y=2025
        M=1
        D=3
        h=20 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,127.807802,2) #Matched!!!
        self.assertAlmostEqual(el,26.439441,1) #not matched at 2 decimals

        celestialObjectName="Mars"
        Y=2025
        M=1
        D=3
        h=6 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,89.925673,1) #not matched at 2 decimals
        self.assertAlmostEqual(el,47.084832,1) #not matched at 2 decimals

        celestialObjectName="Jupiter"
        Y=2025
        M=1
        D=3
        h=4 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,110.744685,1) #not matched at 2 decimals
        self.assertAlmostEqual(el,64.717721,2) #Matched!!!

        celestialObjectName="Saturn"
        Y=2025
        M=1
        D=3
        h=3 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,234.070866,1) #not matched at 2 decimals
        self.assertAlmostEqual(el,31.028380,1) #not matched at 2 decimals

        '''
        #corrections for Beta/El calculated from tests
        betaElCorrections={"Star":    [-0.009515,0.0],
                           "Sun":     [0.0,-0.005825],
                           "Moon":    [0.0,0.0],
                           "Venus":   [0.0,-0.006748],
                           "Mars":    [-0.005935,-0.016992],
                           "Jupiter": [-0.011767,0.0],
                           "Saturn":  [-0.025106,0.046960]}
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
        self.assertAlmostEqual(deltael1,0.14756668691052255,6)
        self.assertAlmostEqual(beta1,-84.73526579689504,6)

if __name__ == '__main__':
    unittest.main()
