import sys
sys.path.append("..\src")

from math import degrees, radians, sqrt, log as ln, sin, cos
from numpy import array as vector

from Vallado import DMStoRad,JulianDate,LSTime,TimeToHMS,RadtoDMS,Sun,GeocentricRadec
from utility import HMSToTime

import almanac

deltaT=32.184+37.0-0.0 #IERS correction

GHAAriesNA=degrees(DMStoRad(245,40.4,0))
print("Nautical almanac GHAAries: ",GHAAriesNA)

GHAAriesAP=almanac.GHAOfAriesAt(2023,10,27,14,0,0)
print("AstroPy GHAAries: ",GHAAriesAP," Deviation from NA: ",GHAAriesNA-GHAAriesAP)

thetaLST,thetaGMST=LSTime(JulianDate(2023,10,27,14,0,0),0,0) #calculating without IERS correction because it's already counted in polynominal
print("Vallado GHAAries: ",thetaGMST," Deviation from NA: ",GHAAriesNA-thetaGMST)

print("==========")

#h,m,s=TimeToHMS(0.5625*86400)
#print(h,m,s)
#J1991_25=JulianDate(1991,4,2,h,m,s)
#print(J1991_25)

#J1991.25 is April 2.5625, 1991 TT or JD 2448349.0625

#JY is 365.25 JD (of 86400 sec) exact
#Sidereal year length is 365.256363004 (according to Wikipedia https://en.wikipedia.org/wiki/Sidereal_year)

def PositionFor(alpha0,delta0,mu_alpha,mu_delta,JD):
    deltatyears=(JD-2448349.0625)/365.25 
    alpha=alpha0+((mu_alpha/3600/1000)*cos(radians(delta0))*deltatyears)
    delta=delta0+((mu_delta/3600/1000)*deltatyears)
    return alpha,delta
    
shaNA=degrees(DMStoRad(80,34.1,0))
deltaNA=degrees(DMStoRad(38,48.5,0))
print("Nautical almanac Vega SHA:",shaNA)
print("Nautical almanac Vega Dec:",deltaNA)

Vega=almanac.GetCelestialObject("Vega")
shaAP=Vega.SHAAt(2023,10,27,14,0,0)
deltaAP=Vega.DecAt(2023,10,27,14,0,0)
print("AstroPy Vega SHA:", shaAP,"Deviation from NA:",shaNA-shaAP)
print("AstroPy Vega Dec:", deltaAP,"Deviation from NA:",deltaNA-deltaAP)

import hipparcos
import simbad

alpha0,delta0,mu_alpha,mu_delta=hipparcos.LoadDataFor(91262)
#alpha0,delta0,mu_alpha,mu_delta=simbad.LoadDataFor("Vega")
alpha,delta=PositionFor(alpha0,delta0,mu_alpha,mu_delta,JulianDate(2023,10,27,14,0,0)+((deltaT/86400.0)/2.0))
sha=360.0-alpha
print("Catalog+Vallado Vega SHA:",sha,"Deviation from NA:",shaNA-sha)
print("Catalog+Vallado Vega Dec:",delta,"Deviation from NA:",deltaNA-delta)

print("==========")

GHASunNA=degrees(DMStoRad(34,1.8,0))
deltaSunNA=-degrees(DMStoRad(12,48.8,0))
print("Nautical almanac Sun GHA:",GHASunNA)
print("Nautical almanac Sun Dec:",deltaSunNA)

Sol=almanac.GetCelestialObject("Sun")
GHASunAP=Sol.GHAAt(2023,10,27,14,0,0)
deltaSunAP=Sol.DecAt(2023,10,27,14,0,0)
print("AstroPy Sun HA:", GHASunAP,"Deviation from NA:",GHASunNA-GHASunAP)
print("AstroPy Sun Dec:", deltaSunAP,"Deviation from NA:",deltaSunNA-deltaSunAP)

vector_rSun=Sun(JulianDate(2023,10,27,14,0,0)+((deltaT/86400.0)/2.0)) # we should not count speed of light in measurements. With this fix ve achieved almodt perfect coincidence with NA
vector_vSun=vector([0,0,0])
#vector_rSunIJK,vector_vSunIJK=IAU2000CIO(vector_rSun,vector_vSun,2023,10,27,HMSToTime(14,0,0),-0.4399619,32,-0.140682,0.333309,GCRF) # we don't need this
rSunVallado,alphaSunVallado,deltaSunVallado,rdotSunVallado,alphadotSunVallado,deltadotSunVallado=GeocentricRadec(vector_rSun,vector_vSun)
GHASunVallado=thetaGMST-alphaSunVallado
print("Vallado Sun GHA:",GHASunVallado," Deviation from NA:",GHASunNA-GHASunVallado)
print("Vallado Sun Dec:",deltaSunVallado," Deviation from NA:",deltaSunNA-deltaSunVallado)

