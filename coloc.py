#Celestial object implementation for working with local catalog
from celestialobject import navigationPlanetNames, celestialObjectDiameters, Rearth, CelestialObject
from catalog import navigationStarNames
from timeprocessor import ToValladoTime
from ephemeris import ThetaGMSTAt,SunAt,MoonAt,PlanetAt
from catalog import LoadDataFor
from Vallado import JulianDate
from trigonometry import cos,arctg

def GHAOfAriesAt(time): #time must be GMT
    Y,M,D,h,m,s=ToValladoTime(time)
    return ThetaGMSTAt(Y,M,D,h,m,s)

#J1991.25 is April 2.5625, 1991 TT or JD 2448349.0625
#JY is 365.25 JD (of 86400 sec) exact
#Sidereal year length is 365.256363004 (according to Wikipedia https://en.wikipedia.org/wiki/Sidereal_year)
def RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s):
    JD=JulianDate(Y,M,D,h,m,s)
    deltatyears=(JD-2448349.0625)/365.25 
    alpha=alpha0+((mu_alpha/3600/1000)*cos(delta0)*deltatyears)
    delta=delta0+((mu_delta/3600/1000)*deltatyears)
    return alpha,delta

class CelestialObjectFromLocalCatalog(CelestialObject):
    def GHAAt(self, time):
        if not self.type=="Star":
            alpha=delta=r=0
            Y,M,D,h,m,s=ToValladoTime(time)
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            GHA=ThetaGMSTAt(Y,M,D,h,m,s)-alpha
            return GHA
        else:
            return 0

    def DecAt(self, time):
        Y,M,D,h,m,s=ToValladoTime(time)
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

    def SHAAt(self, time):
        if self.type=="Star":
            Y,M,D,h,m,s=ToValladoTime(time)
            alpha0,delta0,mu_alpha,mu_delta=LoadDataFor(self.name)
            alpha,delta=RADecAt(alpha0,delta0,mu_alpha,mu_delta,Y,M,D,h,m,s)
            SHA=360.0-alpha
            return SHA
        else:
            return 0

    def SDAt(self, time):
        if not self.type=="Star":
            alpha=delta=r=0
            Y,M,D,h,m,s=ToValladoTime(time)
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            GHA=ThetaGMSTAt(Y,M,D,h,m,s)-alpha
            d=celestialObjectDiameters[self.name]
            D=r-Rearth
            return arctg(d/(2*D))                    
        else:
            return 0

    def HPAt(self, time):
        if not self.type=="Star":
            alpha=delta=r=0
            Y,M,D,h,m,s=ToValladoTime(time)
            if self.type=="Sun":
                alpha,delta,r=SunAt(Y,M,D,h,m,s)
            if self.type=="Moon":
                alpha,delta,r=MoonAt(Y,M,D,h,m,s)
            if self.type=="Planet":
                alpha,delta,r=PlanetAt(self.name,Y,M,D,h,m,s)
            D=r-Rearth
            return arctg(Rearth/D)
        else:
            return 0
