from external.math import sqrt
import external.math as math
import almanac
import angle

def CalculateIntercept(phie,lambdae,Y,M,D,h,m,s,celestialObjectName,Hs,hoe,T=10,P=1010.0,limb=0,IC=0): #based on method described in Bowditch (originally from http://www.tecepe.com.br/nav/inav_met.htm by Omar Reis)
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
        GHA=GHAAries+SHA
    if lambdae<0:
        delta=-delta
    LHA=GHA+lambdae
    Hc=asin((sin(phie)*sin(delta))+(cos(phie)*cos(delta)*cos(LHA)))
    a=angle.Normalize(Ho-Hc)
    if lambdae<0:
        Z=atan(sin(LHA)/((sin(phie)*cos(LHA))-(cos(phie)*tan(delta))))
    #Z=acos((sin(delta)-(sin(phie)*sin(Hc)))/(cos(phie)*cos(Hc)))
    else:
        Z=atan(sin(LHA)/((cos(phie)*tan(delta))-(sin(phie)*cos(LHA)))) #as in Bowditch
    return a,Z
