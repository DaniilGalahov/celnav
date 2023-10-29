import sys
sys.path.append("..\Astrodynamic")

from numpy import array as vector

from Vallado import JulianDate,Sun,GeocentricRadec

navigationPlanets=["Venus",
                   "Mars",
                   "Jupiter",
                   "Saturn"]

deltaT=32.184+37.0-0.0  #IERS correction for 2023    

def ThetaGMSTAt(Y,M,D,h,m,s):
    thetaLST,thetaGMST=LSTime(JulianDate(Y,M,D,h,m,s),0,0) #calculating without IERS correction because it's already counted in polynominal
    return thetaGMST

def SunAt(Y,M,D,h,m,s):
    vector_r=Sun(JulianDate(Y,M,D,h,m,s)+((deltaT/86400.0)/2.0)) #calculating with IERS correction; this way of calculation produces minimal deviation from NA
    vector_v=vector([0,0,0])
    r,alpha,delta,rdot,alphadot,deltadot=GeocentricRadec(vector_r,vector_v)
    return alpha,delta,r
    
