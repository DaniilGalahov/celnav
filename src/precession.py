from external.math import *
from external.astro import *

from ephemeris import UTCtoUT1,UT1toTAI,TAItoTDB
import angle

def AnglesFor(Y,M,D,h,m,s): #following Meeus; for J2000+ only
    deltaT=UTCtoUT1+UT1toTAI+TAItoTDB
    JD=JulianDate(Y,M,D,h,m,s)+(deltaT/86400.0)
    T=(JD-2451545.0)/36525
    zeta=angle.Normalize(((2306.2181*pow(T,1))+(0.30188*pow(T,2))+(0.017998*pow(T,3)))/3600.0)
    z=angle.Normalize(((2306.2181*pow(T,1))+(1.09468*pow(T,2))+(0.018203*pow(T,3)))/3600.0)
    theta=angle.Normalize(((2004.3109*pow(T,1))+(-0.42665*pow(T,2))+(-0.041833*pow(T,3)))/3600.0)
    return zeta,z,theta

def CorrectionFor(alpha0,delta0,zeta,z,theta): #following Meeus
    alpha0=radians(alpha0)
    delta0=radians(delta0)
    zeta=radians(zeta)
    z=radians(z)
    theta=radians(theta)
    A=cos(delta0)*sin(alpha0+zeta)
    B=(cos(theta)*cos(delta0)*cos(alpha0+zeta))-(sin(theta)*sin(delta0))
    C=(sin(theta)*cos(delta0)*cos(alpha0+zeta))+(cos(theta)*sin(delta0))
    deltaalpha=atan2(A,B)
    alpha=deltaalpha+z
    delta=asin(C)
    if degrees(delta0)>89.0:
        delta=acos(sqrt(pow(A,2)+pow(B,2)))
    return degrees(alpha),degrees(delta)    

def RotationMatrixFrom(zeta,z,theta):
    return ROT3(radians(-z))@ROT2(radians(theta))@ROT3(radians(-zeta)) #Idea by ChatGPT
