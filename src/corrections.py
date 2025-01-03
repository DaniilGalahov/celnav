from external.math import *
from external.astro import *

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

def PhiLambdaCorrectionsFor(phi,lambda_,celestialObjectName,Y,M,D,h,m,s):
    phiAP=round(phi)
    lambdaAP=round(lambda_)
