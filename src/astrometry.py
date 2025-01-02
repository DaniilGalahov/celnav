import external.math as math
from external.math import sin, cos, tan, asin, acos, atan, radians, degrees, sqrt, ceil, sign
import almanac
import angle

'''
Below implemented multiple versions of Captain Thomas H. Sumner method to construct a Line-of-Position from a single Altitude measurement

Originally, idea of algorithm was taken from http://www.tecepe.com.br/nav/inav_met.htm (implementation by Omar Reis). His algorithm worked
stable, but it was a version of Bowditch algoritm with calculation of Zn in a way independent on Hc, and without corrections mentioned in
Nautical Almanac. Both algorithms Reis and Bowditch/NA suffered from bad precision using both my almanac or astropy.

Later I implemented my own version of algorithm, providing better precision with my almanac and astropy.
'''

def ApplyElevationCorrectionTo(Hs,hoe=0,T=10,P=1010.0,HP=0,SD=0,limb=0,IC=0):
    Dip=-0.0293*sqrt(hoe) #dip (observer altitude) correction, not same as in Bowditch , but it provides data in decimal degrees for meters
    Sum=IC+Dip
    Ha=Hs+Sum
    R0=0.016667/tan(radians(Ha+(7.31/(Ha+4.4)))) #Bennet formula - from https://thenauticalalmanac.com/Formulas.html#Determine_Refraction_
    f=(P/1013.25)*(283/(273.15+T)) #temperature correction formula, from https://en.wikipedia.org/wiki/Atmospheric_refraction (modified to match valves in Bowditch)
    R=f*R0    
    PA=HP*cos(radians(Ha))    
    Ho=Ha-R+PA-(limb*SD) #in case of measuring by lower limb of sun/moon it must be just "+SD". negative limb means lower limb, positive means upper limb;
    return Ho

def FindLoP(phiDR,lambdaDR,Y,M,D,h,m,s,celestialObjectName,Hs,hoe=0,T=10,P=1010.0,limb=0,IC=0): #based on method described in Nautical Almanac and Bowditch
    celestialObject = almanac.GetCelestialObject(celestialObjectName)
    HP=celestialObject.HPAt(Y,M,D,h,m,s) #horizontal parallax of celestial object
    SD=celestialObject.SDAt(Y,M,D,h,m,s) #semi-diameter of celestial object
    Ho=ApplyElevationCorrectionTo(Hs,hoe,T,P,HP,SD,limb,IC)    
    if not celestialObject.type=="Star":
        GHA=celestialObject.GHAAt(Y,M,D,h,m,s)
        delta=celestialObject.DecAt(Y,M,D,h,m,s)
    else:
        GHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s) #my almanac provided values ALREADY WITH CORRECTIONS
        SHA=celestialObject.SHAAt(Y,M,D,h,m,s)
        delta=celestialObject.DecAt(Y,M,D,h,m,s)
        GHA=angle.Normalize(GHAAries+SHA) #must be normalized for proper calculations later
    phiAP=phiDR
    if lambdaDR<0:
        lambdaAP=lambdaDR+(GHA%1.0)
    else:
        lambdaAP=lambdaDR+(1.0-(GHA%1.0))
    if lambdaAP<0: #in Western longitudes (as said in Nautical Almanac)
        GHA=int(GHA) #we need not rounded but "whole" degrees
        lambdaAP=int(lambdaAP)
        if GHA<lambdaAP:
            GHA+=360.0
        LHA=GHA-lambdaAP
    else:  #in Eastern longitudes (as said in Nautical Almanac)
        lambdaAP=int(lambdaAP)
        GHADifference=ceil(GHA)-GHA #would work correctly only if GHA is normalized
        LHA=GHA+lambdaAP+GHADifference
        if LHA>360.0:
            LHA-=360.0
    Hc=degrees(asin((sin(radians(delta))*sin(radians(phiAP)))+(cos(radians(phiAP))*cos(radians(delta))*cos(radians(LHA)))))
    if sign(delta)!=sign(phiAP):
        delta=-delta
    Z=degrees(acos((sin(radians(delta))-(sin(radians(phiAP))*sin(radians(Hc))))/(cos(radians(phiAP))*cos(radians(Hc))))) #in a way dependent on Hc
    '''
    Z=degrees(atan(sin(radians(LHA))/((cos(radians(phiAP))*tan(radians(delta)))-(sin(radians(phiAP))*cos(radians(LHA)))))) #in a way independent on Hc
    if Z>180.0:
        Z=-Z
    if Z<0:
        Z=180.0+Z
    '''
    a=Ho-Hc
    if phiAP>=0.0:
        if LHA>180.0:
            Zn=Z
        else:
            Zn=360.0-Z
    else:
        if LHA>180.0:
            Zn=180.0-Z
        else:
            Zn=180.0+Z
    return angle.Normalize(a),angle.Normalize(Zn)
