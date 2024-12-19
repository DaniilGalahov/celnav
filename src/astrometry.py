from external.math import sqrt, sin, cos, tan, asin, atan, degrees, radians
import almanac
import angle

def CalculateIntercept(phigce,lambdae,Y,M,D,h,m,s,celestialObjectName,deltats,hoh,T,P,limb=-1): #based on method described on http://www.tecepe.com.br/nav/inav_met.htm by Omar Reis && Bowditch
    celestialObject = almanac.GetCelestialObject(celestialObjectName)
    #(!)here must be instrument correction
    Dip=0.0293*sqrt(hoh) #altitude correction, not same as in Omar Reis manual, but it provides data in decimal degrees for meters (from Bowditch)
    deltat=deltats-Dip
    Ro=0.0167/(tan(radians(deltat+7.31))/(deltat+4.4))#refraction correction. Do not measure objects which are near your astronomical horizon!
    f=(0.28*P)/(T+273)
    R=f*Ro
    #(!)here must be oblateness correction
    HP=celestialObject.HPAt(Y,M,D,h,m,s) #horizontal parallax of celestial object
    PA=HP*cos(radians(deltat))
    SD=celestialObject.SDAt(Y,M,D,h,m,s) #semi-diameter of celestial object
    deltato=deltat-R+PA-(limb*SD) #deltat observed; in case of measuring by lower limb of sun/moon it must be just "+SD". negative limb means lower limb, positive means upper limb
    if not celestialObject.type=="Star":
        GHA=celestialObject.GHAAt(Y,M,D,h,m,s)
        delta=celestialObject.DecAt(Y,M,D,h,m,s)
    else:
        GHAAries=almanac.GHAOfAriesAt(Y,M,D,h,m,s)
        SHA=celestialObject.SHAAt(Y,M,D,h,m,s)
        delta=celestialObject.DecAt(Y,M,D,h,m,s)
        GHA=GHAAries+SHA
    LHA=GHA+lambdae
    phigce=radians(phigce)
    lambdae=radians(lambdae)
    delta=radians(delta)
    LHA=radians(LHA)
    deltatc=degrees(asin((sin(phigce)*sin(delta))+(cos(phigce)*cos(delta)*cos(LHA))))
    p=deltato-deltatc
    z=angle.Normalize(degrees(atan(sin(LHA)/((sin(phigce)*cos(LHA))-(cos(phigce)*tan(delta))))))
    return p,z
