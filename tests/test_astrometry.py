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
                           "Moon":    [0.0,0.0], #???
                           "Venus":   [0.0,-0.006748],
                           "Mars":    [-0.005935,-0.016992],
                           "Jupiter": [-0.011767,0.0],
                           "Saturn":  [-0.025106,0.046960]}
        '''

        celestialObjectName="Mars" #Jan 2021
        Y=2021
        M=1
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,66.129829,1) #not matched at 2 decimals, d=0.007329
        self.assertAlmostEqual(el,-13.058300,1) #not matched at 2 decimals, d=0.010334

        celestialObjectName="Mars" #Feb 2021
        Y=2021
        M=2
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,70.749626,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,2.318123,1) #not matched at 2 decimals, d=0.006324

        celestialObjectName="Mars" #Mar 2021
        Y=2021
        M=3
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,73.066897,2) #matched at 2 decimals
        self.assertAlmostEqual(el,13.728607,2) #matched at 2 decimals

        celestialObjectName="Mars" #Apr 2021
        Y=2021
        M=4
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,75.579792,2) #matched at 2 decimals
        self.assertAlmostEqual(el,23.880917,2) #matched at 2 decimals

        celestialObjectName="Mars" #May 2021
        Y=2021
        M=5
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,79.609758,2) #matched at 2 decimals
        self.assertAlmostEqual(el,31.879873,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jun 2021
        Y=2021
        M=6
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,86.995672,2) #matched at 2 decimals
        self.assertAlmostEqual(el,39.188951,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jul 2021
        Y=2021
        M=7
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,98.601387,2) #matched at 2 decimals
        self.assertAlmostEqual(el,45.787438,2) #matched at 2 decimals

        celestialObjectName="Mars" #Aug 2021
        Y=2021
        M=8
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,116.492857,2) #matched at 2 decimals
        self.assertAlmostEqual(el,51.388414,2) #matched at 2 decimals

        celestialObjectName="Mars" #Sep 2021
        Y=2021
        M=9
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,139.942155,2) #matched at 2 decimals
        self.assertAlmostEqual(el,53.672458,2) #matched at 2 decimals

        celestialObjectName="Mars" #Oct 2021
        Y=2021
        M=10
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,162.885934,2) #matched at 2 decimals
        self.assertAlmostEqual(el,51.107378,2) #matched at 2 decimals

        celestialObjectName="Mars" #Nov 2021
        Y=2021
        M=11
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,180.851868,2) #matched at 2 decimals
        self.assertAlmostEqual(el,44.600148,2) #matched at 2 decimals

        celestialObjectName="Mars" #Dec 2021
        Y=2021
        M=12
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,191.952392,2) #matched at 2 decimals
        self.assertAlmostEqual(el,37.328581,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jan 2022
        Y=2022
        M=1
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,199.194092,2) #matched at 2 decimals
        self.assertAlmostEqual(el,31.391268,2) #matched at 2 decimals

        celestialObjectName="Mars" #Feb 2022
        Y=2022
        M=2
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,204.966168,2) #matched at 2 decimals
        self.assertAlmostEqual(el,28.522019,2) #matched at 2 decimals

        celestialObjectName="Mars" #Mar 2022
        Y=2022
        M=3
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,211.176642,2) #matched at 2 decimals
        self.assertAlmostEqual(el,28.574365,1) #not matched at 2 decimals d=0.006510

        celestialObjectName="Mars" #Apr 2022
        Y=2022
        M=4
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,220.956783,2) #matched at 2 decimals
        self.assertAlmostEqual(el,30.253072,1) #not matched at 2 decimals d=0.006990

        celestialObjectName="Mars" #May 2022
        Y=2022
        M=5
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,233.659388,2) #matched at 2 decimals
        self.assertAlmostEqual(el,31.571729,1) #not matched at 2 decimals d=0.005706

        celestialObjectName="Mars" #Jun 2022
        Y=2022
        M=6
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,248.603073,2) #matched at 2 decimals
        self.assertAlmostEqual(el,31.015297,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jul 2022
        Y=2022
        M=7
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,262.484538,2) #matched at 2 decimals
        self.assertAlmostEqual(el,28.199650,2) #matched at 2 decimals

        celestialObjectName="Mars" #Aug 2022
        Y=2022
        M=8
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,274.592754,2) #matched at 2 decimals
        self.assertAlmostEqual(el,23.114610,2) #matched at 2 decimals

        celestialObjectName="Mars" #Sep 2022
        Y=2022
        M=9
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,284.547645,2) #matched at 2 decimals
        self.assertAlmostEqual(el,15.438274,2) #matched at 2 decimals

        celestialObjectName="Mars" #Oct 2022
        Y=2022
        M=10
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,294.383834,2) #matched at 2 decimals
        self.assertAlmostEqual(el,4.160332,1) #not matched at 2 decimals, d=0.006012

        celestialObjectName="Mars" #Nov 2022
        Y=2022
        M=11
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,310.731876,1) #not matched at 2 decimals, d=0.011062
        self.assertAlmostEqual(el,-13.057767,1) #not matched at 2 decimals, d=0.006898

        celestialObjectName="Mars" #Dec 2022
        Y=2022
        M=12
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,343.465542,1) #not matched at 2 decimals, d=0.025721
        self.assertAlmostEqual(el,-29.750157,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jan 2023
        Y=2023
        M=1
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,25.481056,1) #not matched at 2 decimals, d=0.024646
        self.assertAlmostEqual(el,-27.473295,1) #not matched at 2 decimals, d=0.009557

        celestialObjectName="Mars" #Feb 2023
        Y=2023
        M=2
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,48.077157,1) #not matched at 2 decimals, d=0.013360
        self.assertAlmostEqual(el,-13.144393,1) #not matched at 2 decimals, d=0.011181

        celestialObjectName="Mars" #Mar 2023
        Y=2023
        M=3
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,58.205684,1) #not matched at 2 decimals, d=0.007488
        self.assertAlmostEqual(el,-1.072604,1) #not matched at 2 decimals, d=0.008373

        celestialObjectName="Mars" #Apr 2023
        Y=2023
        M=4
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,65.901470,2) #matched at 2 decimals
        self.assertAlmostEqual(el,9.705300,1) #not matched at 2 decimals, d=0.005934

        celestialObjectName="Mars" #May 2023
        Y=2023
        M=5
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,73.333260,2) #matched at 2 decimals
        self.assertAlmostEqual(el,18.303946,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jun 2023
        Y=2023
        M=6
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,82.907944,2) #matched at 2 decimals
        self.assertAlmostEqual(el,26.270017,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jul 2023
        Y=2023
        M=7
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,95.064913,2) #matched at 2 decimals
        self.assertAlmostEqual(el,33.443421,2) #matched at 2 decimals

        celestialObjectName="Mars" #Aug 2023
        Y=2023
        M=8
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,111.261763,2) #matched at 2 decimals
        self.assertAlmostEqual(el,39.632821,2) #matched at 2 decimals

        celestialObjectName="Mars" #Sep 2023
        Y=2023
        M=9
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,130.610710,2) #matched at 2 decimals
        self.assertAlmostEqual(el,43.013158,2) #matched at 2 decimals

        celestialObjectName="Mars" #Oct 2023
        Y=2023
        M=10
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,149.417843,2) #matched at 2 decimals
        self.assertAlmostEqual(el,42.491033,2) #matched at 2 decimals

        celestialObjectName="Mars" #Nov 2023
        Y=2023
        M=11
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,165.007096,2) #matched at 2 decimals
        self.assertAlmostEqual(el,38.863282,2) #matched at 2 decimals

        celestialObjectName="Mars" #Dec 2023
        Y=2023
        M=12
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,175.108136,1) #not matched at 2 decimals, d=0.006286
        self.assertAlmostEqual(el,34.794489,2) #matched at 2 decimals
        
        celestialObjectName="Mars" #Jan 2024
        Y=2024
        M=1
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,181.859821,1) #not matched at 2 decimals, d=0.008151
        self.assertAlmostEqual(el,32.605032,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Feb 2024
        Y=2024
        M=2
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,187.660937,1) #not matched at 2 decimals, d=0.008712
        self.assertAlmostEqual(el,33.889519,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Mar 2024
        Y=2024
        M=3
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,194.945131,1) #not matched at 2 decimals, d=0.007257
        self.assertAlmostEqual(el,37.954797,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Apr 2024
        Y=2024
        M=4
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,207.010441,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,43.515959,2) #matched at 2 decimals!

        celestialObjectName="Mars" #May 2024
        Y=2024
        M=5
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,223.361042,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,47.602089,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Jun 2024
        Y=2024
        M=6
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,242.292627,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,48.600179,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Jul 2024
        Y=2024
        M=7
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,258.191915,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,46.435728,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Aug 2024
        Y=2024
        M=8
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,269.696850,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,41.880383,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Sep 2024
        Y=2024
        M=9
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,276.772593,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,35.142762,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Oct 2024
        Y=2024
        M=10
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,281.655503,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,25.808144,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Nov 2024
        Y=2024
        M=11
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,287.968989,2) #matched at 2 decimals!
        self.assertAlmostEqual(el,12.263974,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Dec 2024
        Y=2024
        M=12
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,299.881825,1) #not matched at 2 decimals! d=0.006901
        self.assertAlmostEqual(el,-5.273704,2) #matched at 2 decimals!

        celestialObjectName="Mars" #Jan 2025
        Y=2025
        M=1
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,327.308560,1) #not matched at 2 decimals, d=0.012208
        self.assertAlmostEqual(el,-25.026752,2) #matched at 2 decimals

        celestialObjectName="Mars" #Feb 2025
        Y=2025
        M=2
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,10.710728,1) #not matched at 2 decimals, d=0.012339
        self.assertAlmostEqual(el,-29.675436,1) #not matched at 2 decimals, d=0.007050

        celestialObjectName="Mars" #Mar 2025
        Y=2025
        M=3
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,38.443605,1) #not matched at 2 decimals, d=0.007363
        self.assertAlmostEqual(el,-19.411782,1) #not matched at 2 decimals, d=0.007816

        celestialObjectName="Mars" #Apr 2025
        Y=2025
        M=4
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,55.607465,2) #matched at 2 decimals
        self.assertAlmostEqual(el,-6.837786,1) #not matched at 2 decimals, d=0.005925

        celestialObjectName="Mars" #May 2025
        Y=2025
        M=5
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,67.705098,2) #matched at 2 decimals
        self.assertAlmostEqual(el,3.410856,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jun 2025
        Y=2025
        M=6
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,79.824935,2) #matched at 2 decimals
        self.assertAlmostEqual(el,12.642417,2) #matched at 2 decimals

        celestialObjectName="Mars" #Jul 2025
        Y=2025
        M=7
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,92.788322,2) #matched at 2 decimals
        self.assertAlmostEqual(el,20.621303,2) #matched at 2 decimals

        celestialObjectName="Mars" #Aug 2025
        Y=2025
        M=8
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,108.013771,2) #matched at 2 decimals
        self.assertAlmostEqual(el,27.333368,2) #matched at 2 decimals

        celestialObjectName="Mars" #Sep 2025
        Y=2025
        M=9
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,124.484862,2) #matched at 2 decimals
        self.assertAlmostEqual(el,31.363812,2) #matched at 2 decimals

        celestialObjectName="Mars" #Oct 2025
        Y=2025
        M=10
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,139.554422,2) #matched at 2 decimals
        self.assertAlmostEqual(el,32.166061,2) #matched at 2 decimals

        celestialObjectName="Mars" #Nov 2025
        Y=2025
        M=11
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,151.702985,2) #matched at 2 decimals
        self.assertAlmostEqual(el,30.858514,2) #matched at 2 decimals

        celestialObjectName="Mars" #Dec 2025
        Y=2025
        M=12
        D=3
        h=19 #UTC
        m=0
        s=0
        beta,el=astrometry.BetaElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.        
        self.assertAlmostEqual(beta,159.322968,2) #matched at 2 decimals
        self.assertAlmostEqual(el,29.842295,2) #matched at 2 decimals

        
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
        self.assertAlmostEqual(deltael1,0.12919942195004097,6)
        self.assertAlmostEqual(beta1,-84.73904924679685,6)

if __name__ == '__main__':
    unittest.main()
