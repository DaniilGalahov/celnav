#Extended algorithms created following user requests.
#After practical testing can be added to main library

from external.math import *
from external.astro import JulianDate, ROT3
from timeprocessor import LTtoGMT
from astrometry import FindToCoEE, ElevationCorrection
from position import FromToCoEEo2CO


#Sight reduction without elevation correction
def CoarseSightReduction(phiAP,lambdaAP,
                         Y,M,D,h,m,s,
                         celestialObjectName,
                         el):
    return FindToCoEE(phiAP,lambdaAP,Y,M,D,h,m,s,celestialObjectName,el)

#Functions for dynamic fix
class Dynamic:
    @staticmethod
    def LTToGMT(Yl,Ml,Dl,hl,ml,sl,lambdaDR,APCorr):
        lambdaDR=lambdaDR+APCorr[0]
        return LTtoGMT(Yl,Ml,Dl,hl,ml,sl,lambdaDR)

    @staticmethod
    def TimeDelta(Y1,M1,D1,h1,m1,s1,
                  Y2,M2,D2,h2,m2,s2):
        JD1=JulianDate(Y1,M1,D1,h1,m1,s1)
        JD2=JulianDate(Y2,M2,D2,h2,m2,s2)
        dt=(JD2-JD1)*24.0
        return dt

    @staticmethod
    def ZeroCorrection():
        return vector([0,0,0])

    @staticmethod
    def APCorrection(z,v,dt):
        z=radians(z)
        d=(v*dt)/60.0
        vector_N=vector([0,1,0])
        vector_C=dot(ROT3(z),vector_N)*d
        return vector_C

    @staticmethod
    def SightReduction(phiAP,lambdaAP,
                       APCorr,
                       Y,M,D,h,m,s,
                       celestialObjectName,el,
                       indexCorrection=0,hoe=0,T=10,P=1010.0,limb=0):
        phiAP=phiAP+APCorr[1]
        lambdaAP=lambdaAP+APCorr[0]
        el=el+ElevationCorrection(celestialObjectName,Y,M,D,h,m,s,el,indexCorrection,hoe,T,P,limb)
        return FindToCoEE(phiAP,lambdaAP,Y,M,D,h,m,s,celestialObjectName,el)

    @staticmethod
    def Fix(phiAP,lambdaAP,
            APCorr,
            a1,Z1,
            a2,Z2):
        phiAP=phiAP+APCorr[1]
        lambdaAP=lambdaAP+APCorr[0]
        return FromToCoEEo2CO(phiAP,lambdaAP,a1,Z1,a2,Z2)
