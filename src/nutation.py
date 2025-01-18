#Functions to calculate nutation of the Earth
from external.math import *
from external.astro import *

from ephemeris import UTCtoUT1,UT1toTAI,TAItoTDB
import angle

def AnglesFor(Y,M,D,h,m,s): #follow Meeus (ChatGPT tried to follow Meeus but did not understand details)
    deltaT=UTCtoUT1+UT1toTAI+TAItoTDB
    JD=JulianDate(Y,M,D,h,m,s)+(deltaT/86400.0)
    T=(JD-2451545.0)/36525
    Omega=radians(angle.Normalize(125.04452+(-1934.136261*pow(T,1))+(0.0020708*pow(T,2))+(pow(T,3)/450000))) #GPT made a mistake here - mess zeros
    LSun=radians(angle.Normalize(280.4665+(36000.7698*T)))
    LMoon=radians(angle.Normalize(218.3165+(481267.8813*T))) ##GPT made a mistake here - totally wrong numbers
    deltaPsi=angle.ToSigned180(((-17.20*sin(Omega))+(-1.32*sin(2*LSun))+(-0.23*sin(2*LMoon))+(0.21*sin(2*Omega)))/3600.0) #GPT made a mistake here - replaced the numbers
    deltaEpsilon=angle.ToSigned180(((9.20*cos(Omega))+(0.57*cos(2*LSun))+(0.10*cos(2*LMoon))+(-0.09*cos(2*Omega)))/3600.0)
    epsilon=angle.ToSigned180(23.439291+(-0.0130042*pow(T,1))+(-0.0000001639*pow(T,2))+(0.0000005036*pow(T,3)))
    return deltaPsi,deltaEpsilon,epsilon

def CorrectionFor(alpha,delta,deltaPsi,deltaEpsilon,epsilon): #following Meeus, p.151
    alpha=radians(alpha)
    delta=radians(delta)
    deltaPsi=radians(deltaPsi)
    deltaEpsilon=radians(deltaEpsilon)
    epsilon=radians(epsilon)
    deltaalpha1=((cos(epsilon)+(sin(epsilon)*sin(alpha)*tan(delta)))*deltaPsi)-((cos(alpha)*tan(delta))*deltaEpsilon)
    deltadelta1=((sin(epsilon)*cos(alpha))*deltaEpsilon)+(sin(alpha)*deltaEpsilon)
    alpha1=alpha+deltaalpha1
    delta1=delta+deltadelta1
    return degrees(alpha1),degrees(delta1)

'''
def RotationMatrixFrom(deltaPsi,deltaEpsilon,epsilon):
    return ROT1(radians(-epsilon))@ROT3(radians(deltaPsi))@ROT1(radians(epsilon+deltaEpsilon)) #Idea by ChatGPT
'''
