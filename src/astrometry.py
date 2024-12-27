import external.math as math
from external.math import sqrt, ceil, sign
import almanac
import angle

def CalculateIntercept(phiDR,lambdaDR,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,T=10,P=1010.0,limb=0,IC=0): #based on method described in Bowditch (originally from http://www.tecepe.com.br/nav/inav_met.htm by Omar Reis)
    def sin(x):
        return math.sin(math.radians(x))
    def cos(x):
        return math.cos(math.radians(x))
    def tan(x):
        return math.tan(math.radians(x))
    def asin(x):
        return math.degrees(math.asin(x))
    def acos(x):
        return math.degrees(math.acos(x))
    def atan(x):
        return math.degrees(math.atan(x))
    celestialObject = almanac.GetCelestialObject(celestialObjectName)
    Dip=-0.0293*sqrt(hoe) #dip (observer altitude) correction, not same as in Bowditch , but it provides data in decimal degrees for meters
    Sum=IC+Dip
    Ha=Hs+Sum
    R0=0.016667/tan(Ha+(7.31/(Ha+4.4))) #Bennet formula - from https://thenauticalalmanac.com/Formulas.html#Determine_Refraction_
    f=(P/1013.25)*(283/(273.15+T)) #temperature correction formula, from https://en.wikipedia.org/wiki/Atmospheric_refraction (modified to match valves in Bowditch)
    R=f*R0
    HP=celestialObject.HPAt(Y,M,D,h,m,s) #horizontal parallax of celestial object
    PA=HP*cos(Ha)
    SD=celestialObject.SDAt(Y,M,D,h,m,s) #semi-diameter of celestial object
    Ho=Ha-R+PA-(limb*SD) #in case of measuring by lower limb of sun/moon it must be just "+SD". negative limb means lower limb, positive means upper limb;
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
    else:  #in Western longitudes (as said in Nautical Almanac)
        lambdaAP=int(lambdaAP)
        GHADifference=ceil(GHA)-GHA #would work correctly only if GHA is normalized
        LHA=GHA+lambdaAP+GHADifference
        if LHA>360.0:
            LHA-=360.0
    Hc=asin((sin(delta)*sin(phiAP))+(cos(phiAP)*cos(delta)*cos(LHA)))
    if sign(delta)!=sign(phiAP):
        delta=-delta
    Z=acos((sin(delta)-(sin(phiAP)*sin(Hc)))/(cos(phiAP)*cos(Hc))) #in a way dependent on Hc
    '''
    Z=atan(sin(LHA)/((cos(phiAP)*tan(delta))-(sin(phiAP)*cos(LHA)))) #in a way independent on Hc
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
