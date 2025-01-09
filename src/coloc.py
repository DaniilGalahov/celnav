#Celestial object implementation for working with local catalog
from external.math import *
from external.astro import *

from celestialobject import navigationPlanetNames, celestialObjectDiameters, Rearth, SMADione, SMAPhobos, CelestialObject
from catalog import navigationStarNames
from ephemeris import UTCtoUT1,UT1toTAI,TAItoTDB,ThetaGMSTAt,VectorToSunAt,VectorToMoonAt,VectorToPlanetAt,SunRADecAt,MoonRADecAt,PlanetRADecAt
from catalog import LoadDataFor
import precession
import angle

def GHAOfAriesAt(Y,M,D,h,m,s): #time must be GMT
    return angle.Normalize(ThetaGMSTAt(Y,M,D,h,m,s))  #must be normalized to match values from Nautical Almanac

#J1991.25 is April 2.5625, 1991 TT or JD 2448349.0625
#JY is 365.25 JD (of 86400 sec) exact
#Sidereal year length is 365.256363004 (according to Wikipedia https://en.wikipedia.org/wiki/Sidereal_year)
def RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s):
    alpha0=radians(alpha0)
    delta0=radians(delta0)
    mu_alpha=radians(mu_alpha)
    mu_delta=radians(mu_delta)
    deltaT=UTCtoUT1+UT1toTAI+TAItoTDB
    JD=JulianDate(Y,M,D,h,m,s)+(deltaT/86400.0)
    deltatyears=(JD-2448349.0625)/365.25
    alpha=alpha0+((mu_alpha/3600/1000)*cos(delta0)*deltatyears)
    delta=delta0+((mu_delta/3600/1000)*deltatyears)
    return degrees(alpha),degrees(delta)

'''
def NutationAnglesFor(Y,M,D,h,m,s): #follow Meeus (ChatGPT tried to follow Meeus but did not understand details)
    deltaT=UTCtoUT1+UT1toTAI+TAItoTDB
    JD=JulianDate(Y,M,D,h,m,s)+(deltaT/86400.0)
    T=(JD-2451545.0)/36525
    Omega=radians(angle.Normalize(125.04452+(-1934.136261*pow(T,1))+(0.0020708*pow(T,2))+(pow(T,3)/450000))) #GPT made a mistake here - mess zeros
    LSun=radians(angle.Normalize(280.4665+(36000.7698*T)))
    LMoon=radians(angle.Normalize(218.3165+(481267.8813*T))) ##GPT made a mistake here - totally wrong numbers
    deltaPsi=angle.Normalize(((-17.20*sin(Omega))+(-1.32*sin(2*LSun))+(-0.23*sin(2*LMoon))+(0.21*sin(2*Omega)))/3600.0) #GPT made a mistake here - replaced the numbers
    deltaEpsilon=angle.Normalize(((9.20*cos(Omega))+(0.57*cos(2*LSun))+(0.10*cos(2*LMoon))+(-0.09*cos(2*Omega)))/3600.0)
    epsilon=angle.Normalize(23.439291-(0.0130042*T)) #2 last terms omitted
    return deltaPsi,deltaEpsilon,epsilon

def NutationMatrixFor(deltaPsi,deltaEpsilon,epsilon):
    return ROT1(radians(-epsilon))@ROT3(radians(deltaPsi))@ROT1(radians(epsilon+deltaEpsilon)) #Idea by ChatGPT
'''

class CelestialObjectFromLocalCatalog(CelestialObject):
    def VectorAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            vector_r=vector([0,0,0])
            if self.type=="Sun":
                vector_r=VectorToSunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                vector_r=VectorToMoonAt(Y,M,D,h,m,s)
                SD=self.SDAt(Y,M,D,h,m,s)
                vector_r=dot(ROT2(radians(2.0*SD))@ROT3(radians(-2.0*SD)),vector_r)
            if self.type=="Planet":
                vector_r=VectorToPlanetAt(self.name,Y,M,D,h,m,s)
                if self.name=="Venus":
                    SD=self.SDAt(Y,M,D,h,m,s)
                    vector_r=dot(ROT2(radians(-SD))@ROT3(radians(SD)),vector_r) #they measuring vector not to center of Venus but to a corner of Venus image on telescope photo?
                if self.name=="Mars":
                    d=celestialObjectDiameters[self.name]
                    c=SMAPhobos/(0.5*d) #they threatening not the Mars itself, but system Mars-Phobos?
                    SD=self.SDAt(Y,M,D,h,m,s)
                    vector_r=dot(ROT2(radians(2*c*SD))@ROT3(radians(-2*c*SD)),vector_r) #they measuring vector not to center of Mars but to a corner of Mars image on telescope photo?
                if self.name=="Jupiter":
                    SD=self.SDAt(Y,M,D,h,m,s)
                    vector_r=dot(ROT2(radians(SD))@ROT3(radians(-SD)),vector_r)
                if self.name=="Saturn":
                    d=celestialObjectDiameters[self.name]
                    c3=SMADione/(0.5*d) #same as with Mars
                    c2=0.5*c3                    
                    SD=self.SDAt(Y,M,D,h,m,s)
                    vector_r=dot(ROT2(radians(2.0*c2*SD))@ROT3(radians(-2.0*c3*SD)),vector_r) #same as with Mars
            return vector_r               
        else:
            alpha0,delta0,mu_alpha,mu_delta=LoadDataFor(self.name)
            alpha,delta=RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s)
            alpha=radians(alpha)
            delta=radians(delta)
            r=75*1.495978707e+11 #75 AU, position outside the Kuiper belt. I.e., FAR
            i=r*cos(delta)*cos(alpha)
            j=r*cos(delta)*sin(alpha)
            k=r*sin(delta)
            vector_r=vector([i,j,k])
            zeta,z,theta=precession.AnglesFor(Y,M,D,h,m,s)
            P=precession.RotationMatrixFrom(zeta,z,theta)
            vector_r=dot(P,vector_r)
            return vector_r
    
    def GHAAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            alpha=delta=0
            if self.type=="Sun":
                alpha,delta=SunRADecAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta=MoonRADecAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta=PlanetRADecAt(self.name,Y,M,D,h,m,s)
            GHA=angle.Normalize(ThetaGMSTAt(Y,M,D,h,m,s)-alpha)  #must be normalized to match values from Nautical Almanac
            return GHA
        else:
            return 0

    def DecAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            alpha=delta=0
            if self.type=="Sun":
                alpha,delta=SunRADecAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta=MoonRADecAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta=PlanetRADecAt(self.name,Y,M,D,h,m,s)
            return delta
        else:
            alpha0,delta0,mu_alpha,mu_delta=LoadDataFor(self.name)
            alpha,delta=RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s)
            return delta

    def SHAAt(self,Y,M,D,h,m,s):
        if self.type=="Star":
            alpha0,delta0,mu_alpha,mu_delta=LoadDataFor(self.name)
            alpha,delta=RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s)
            SHA=angle.Normalize(360.0-alpha)
            return SHA
        else:
            return 0

    def SDAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            r=0
            if self.type=="Sun":
                r=magnitude(VectorToSunAt(Y,M,D,h,m,s))
            if self.type=="Moon":
                r=magnitude(VectorToMoonAt(Y,M,D,h,m,s))
            if self.type=="Planet":
                r=magnitude(VectorToPlanetAt(self.name,Y,M,D,h,m,s))
            d=celestialObjectDiameters[self.name]
            D=r-Rearth
            return degrees(atan(d/(2*D)))                    
        else:
            return 0

    def HPAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            r=0
            if self.type=="Sun":
                r=magnitude(VectorToSunAt(Y,M,D,h,m,s))
            if self.type=="Moon":
                r=magnitude(VectorToMoonAt(Y,M,D,h,m,s))
            if self.type=="Planet":
                r=magnitude(VectorToPlanetAt(self.name,Y,M,D,h,m,s))
            D=r-Rearth
            return degrees(atan(Rearth/D))
        else:
            return 0
