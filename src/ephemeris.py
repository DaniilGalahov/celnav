from external.math import vector
from external.astro import JulianDate, LSTime, Sun, GeocentricRadec, Moon, PlanetRV, IAU2000CIO, IAU76FK5, HMSToTime

navigationPlanets=["Venus",
                   "Mars",
                   "Jupiter",
                   "Saturn"]

TAItoTDB=32.184 #from precision time to barycentric time (required for calculation of ephemerides)
UT1toTAI=37.0 #from UT1 to precision atomic time
UTCtoUT1=-0.1 #IERS correction for 2024-2025, from civilian time to UT1

deltaUT1=UTCtoUT1
deltaAT=UT1toTAI
xp=-0.140682
yp=0.333309

def ThetaGMSTAt(Y,M,D,h,m,s):
    thetaLST,thetaGMST=LSTime(JulianDate(Y,M,D,h,m,s)+(UTCtoUT1/86400.0),0,0) #calculating without IERS correction because it's already counted in polynominal
    return thetaGMST

def SunAt(Y,M,D,h,m,s):
    vector_r=Sun(JulianDate(Y,M,D,h,m,s)+(UTCtoUT1/86400.0)) 
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r

def MoonAt(Y,M,D,h,m,s):
    vector_r=Moon(JulianDate(Y,M,D,h,m,s)+((UTCtoUT1+UT1toTAI+TAItoTDB)/86400.0))
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r

def PlanetAt(planetName,Y,M,D,h,m,s):
    vector_rPlanetFromSun,vector_vPlanetFromSun=PlanetRV(planetName,JulianDate(Y,M,D,h,m,s))
    vector_rEarthToSun=Sun(JulianDate(Y,M,D,h,m,s)+(UTCtoUT1/86400.0))
    vector_r=vector_rPlanetFromSun+vector_rEarthToSun
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r
    
