#Astrometry functions for navigation purposes
from external.math import *
from external.astro import *

import almanac
import angle
from ephemeris import TAItoTDB, UT1toTAI, UTCtoUT1
from frame import IJK2SEZ

'''
Originally this module included an implemented version of Captain Thomas H. Sumner method to construct a Line-of-Position from a single
Altitude measurement (method "FindLoP")

Initially, idea of algorithm was taken from http://www.tecepe.com.br/nav/inav_met.htm (implementation by Omar Reis). His algorithm worked
stable. Later I implemented a version of algoritm described in Bowditch, in a way how it was explained in Nautical Almanac. This version
did not work well, suffered from bad precision and errors of math.

"FindToCoEE" is my own version of algorithm, based on simplier concepts of vector operations (common in astrodynamics).
'''

def AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s): #mostly for precision testing purposes;
    celestialObject = almanac.GetCelestialObject(celestialObjectName)
    vector_rCO=celestialObject.VectorAt(Y,M,D,h,m,s)
    thetaLST,thetaGMST=LSTime(JulianDate(Y,M,D,h,m,s)+(UTCtoUT1/86400.0),0,lambda_)
    vector_rSite,vector_vSite=Site(phi,0,thetaLST)
    vector_rCOfromSite=vector_rCO+vector_rSite
    vector_dCOfromSite=vector_rCOfromSite/magnitude(vector_rCOfromSite)
    vector_dCOfromSite_SEZ=IJK2SEZ(vector_dCOfromSite,phi,thetaLST)
    vector_Z_SEZ=vector([0,0,1])
    el=90.0-angleBetween(vector_Z_SEZ,vector_dCOfromSite_SEZ)
    vector_N_SEZ=vector([-1,0,0])
    az=angle.Normalize(-signedAngleBetween(vector_N_SEZ,vector_dCOfromSite_SEZ,vector_Z_SEZ)) #we need return azimuth with "-", to match azimuths from Horizons and NAOJ
    return az,el

def ElevationCorrection(celestialObjectName,Y,M,D,h,m,s,Hs,IC=0,hoe=0,T=10,P=1010.0,limb=0):
    Dip=-0.0293*sqrt(hoe) #dip (observer altitude) correction, not same as in Bowditch , but it provides data in decimal degrees for meters
    Sum=IC+Dip
    Ha=Hs+Sum
    R0=0.016667/tan(radians(Ha+(7.31/(Ha+4.4)))) #Bennet formula - from https://thenauticalalmanac.com/Formulas.html#Determine_Refraction_
    f=(P/1013.25)*(283/(273.15+T)) #temperature correction formula, from https://en.wikipedia.org/wiki/Atmospheric_refraction (modified to match valves in Bowditch)
    R=f*R0
    celestialObject = almanac.GetCelestialObject(celestialObjectName)
    HP=celestialObject.HPAt(Y,M,D,h,m,s)
    PA=HP*cos(radians(Ha))
    SD=celestialObject.SDAt(Y,M,D,h,m,s)
    LC=0
    if limb!=0:
        LC=-sign(limb)*SD
    Ho=Ha-R+PA+LC #negative limb means lower limb, positive means upper limb;
    return Ho-Hs

def FindToCoEE(phiAP,lambdaAP,Y,M,D,h,m,s,celestialObjectName,el): #consuming ONLY ALREADY CORRECTED elevation
    celestialObject = almanac.GetCelestialObject(celestialObjectName)
    vector_rCO=celestialObject.VectorAt(Y,M,D,h,m,s)
    thetaLST,thetaGMST=LSTime(JulianDate(Y,M,D,h,m,s)+(UTCtoUT1/86400.0),0,lambdaAP)
    vector_rAP,vector_vAP=Site(phiAP,0,thetaLST)
    vector_rCOfromAP=vector_rCO+vector_rAP
    vector_dCOfromAP=vector_rCOfromAP/magnitude(vector_rCOfromAP)
    vector_dCOfromAP_SEZ=IJK2SEZ(vector_dCOfromAP,phiAP,thetaLST)
    vector_Z_SEZ=vector([0,0,1])
    elAP=90.0-angleBetween(vector_Z_SEZ,vector_dCOfromAP_SEZ)
    deltael=el-elAP
    vector_N_SEZ=vector([-1,0,0])
    beta=signedAngleBetween(vector_N_SEZ,vector_dCOfromAP_SEZ,vector_Z_SEZ)
    return deltael,beta
