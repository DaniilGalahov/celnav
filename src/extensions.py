#Extended algorithms created following user requests.
#After practical testing can be added to main library

from external.math import *
from external.astro import JulianDate
from astrometry import ElevationCorrection, FindToCoEE
from position import FromToCoEEo2CO


#Sight reduction with elevation correction control
def SightReductionCC(phiAP,lambdaAP,
                     Y,M,D,h,m,s,
                     celestialObjectName,
                     el,
                     correctElevation=True,
                     indexCorrection=0,hoe=0,T=10,P=1010.0,limb=0):
    if correctElevation:
        el=el+ElevationCorrection(celestialObjectName,Y,M,D,h,m,s,el,indexCorrection,hoe,T,P,limb)
    return FindToCoEE(phiAP,lambdaAP,Y,M,D,h,m,s,celestialObjectName,el)

def DriftCorrection(Y1,M1,D1,h1,m1,s1,
                    a1,Z1,
                    Y2,M2,D2,h2,m2,s2,
                    z,v):
    z=radians(z)
    Z1=radians(Z1)
    JD1=JulianDate(Y1,M1,D1,h1,m1,s1)
    JD2=JulianDate(Y2,M2,D2,h2,m2,s2)
    dt=(JD2-JD1)*24.0
    #print("dt:",dt)
    d=(v*dt)/60.0
    #print("d:", d)
    a1=a1+(d*cos(z+Z1)) #why? Because we need to SUM (!!!) all affections on coordinates
    #print("a1corr:",a1)
    return a1
