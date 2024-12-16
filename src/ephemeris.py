from external import vector, JulianDate, LSTime, Sun, GeocentricRadec, Moon, PlanetRV

navigationPlanets=["Venus",
                   "Mars",
                   "Jupiter",
                   "Saturn"]

#deltaT=32.184+37.0-0.0  #IERS correction for 2022-2023
deltaT=32.184+37.0-0.1   #IERS correction for 2024-2025

def CorrectedJulianDate(Y,M,D,h,m,s):
    return JulianDate(Y,M,D,h,m,s)+((deltaT/86400.0)/2.0) #calculating with IERS correction; this way of calculation produces minimal deviation from NA

def ThetaGMSTAt(Y,M,D,h,m,s):
    thetaLST,thetaGMST=LSTime(JulianDate(Y,M,D,h,m,s),0,0) #calculating without IERS correction because it's already counted in polynominal
    return thetaGMST

def SunAt(Y,M,D,h,m,s):
    vector_r=Sun(CorrectedJulianDate(Y,M,D,h,m,s)) 
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r

def MoonAt(Y,M,D,h,m,s):
    vector_r=Moon(CorrectedJulianDate(Y,M,D,h,m,s))
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r

def PlanetAt(planetName,Y,M,D,h,m,s):
    vector_rPlanetFromSun,vector_vPlanetFromSun=PlanetRV(planetName,CorrectedJulianDate(Y,M,D,h,m,s))
    vector_rEarthToSun=Sun(CorrectedJulianDate(Y,M,D,h,m,s))
    vector_r=vector_rPlanetFromSun+vector_rEarthToSun
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r
    
