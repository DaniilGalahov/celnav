#Celestial object implementation for working with local catalog
from external.math import cos, atan, degrees, radians
from external.astro import JulianDate

from celestialobject import navigationPlanetNames, celestialObjectDiameters, Rearth, CelestialObject
from catalog import navigationStarNames
from ephemeris import ThetaGMSTAt,SunAt,MoonAt,PlanetAt
from catalog import LoadDataFor
from angle import Normalize

def GHAOfAriesAt(Y,M,D,h,m,s): #time must be GMT
    return Normalize(ThetaGMSTAt(Y,M,D,h,m,s))  #must be normalized to match values from Nautical Almanac

#J1991.25 is April 2.5625, 1991 TT or JD 2448349.0625
#JY is 365.25 JD (of 86400 sec) exact
#Sidereal year length is 365.256363004 (according to Wikipedia https://en.wikipedia.org/wiki/Sidereal_year)
def RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s):
    alpha0=radians(alpha0)
    delta0=radians(delta0)
    mu_alpha=radians(mu_alpha)
    mu_delta=radians(mu_delta)
    JD=JulianDate(Y,M,D,h,m,s)
    deltatyears=(JD-2448349.0625)/365.25 
    alpha=alpha0+((mu_alpha/3600/1000)*cos(delta0)*deltatyears)
    delta=delta0+((mu_delta/3600/1000)*deltatyears)
    return degrees(alpha),degrees(delta)

class CelestialObjectFromLocalCatalog(CelestialObject):
    def GHAAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            alpha=delta=r=0
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            GHA=Normalize(ThetaGMSTAt(Y,M,D,h,m,s)-alpha)  #must be normalized to match values from Nautical Almanac
            return GHA
        else:
            return 0

    def DecAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            alpha=delta=r=0
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            return delta
        else:
            alpha0,delta0,mu_alpha,mu_delta=LoadDataFor(self.name)
            alpha,delta=RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s)
            return delta

    def SHAAt(self,Y,M,D,h,m,s):
        if self.type=="Star":
            alpha0,delta0,mu_alpha,mu_delta=LoadDataFor(self.name)
            alpha,delta=RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s)
            SHA=360.0-alpha
            return SHA
        else:
            return 0

    def SDAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            alpha=delta=r=0
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            GHA=ThetaGMSTAt(Y,M,D,h,m,s)-alpha
            d=celestialObjectDiameters[self.name]
            D=r-Rearth
            return degrees(atan(d/(2*D)))                    
        else:
            return 0

    def HPAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            alpha=delta=r=0
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            D=r-Rearth
            return degrees(atan(Rearth/D))
        else:
            return 0
