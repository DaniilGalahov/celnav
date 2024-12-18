#Celestial object implementation for working with astropy
from external.math import degrees, atan
from external.astro import Time, get_body, solar_system_ephemeris, Angle, EarthLocation, SkyCoord, Distance, u
from celestialobject import navigationPlanetNames, celestialObjectDiameters, Rearth, CelestialObject
from catalog import navigationStarNames
from timeprocessor import YMDhmsToAPyTime

ephemeris='builtin' #can be 'jpl' or 'de432s', but even in this case we have difference with Omar Reis about +14.5' in GHA and about -7' in Dec

def GHAOfAriesAt(time): #time must be GMT
    time = Time(time)
    siderealTime = time.sidereal_time('apparent', 'greenwich')
    return Angle(siderealTime).deg

class CelestialObjectFromAstroPy(CelestialObject):
    def GHAAt(self,Y,M,D,h,m,s):
        time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
        if not self.type=="Star":            
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            GHA=GHAOfAriesAt(time)-body.ra.value 
            return GHA
        else:
            return 0

    def DecAt(self,Y,M,D,h,m,s):
        time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
        if not self.type=="Star":            
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            return body.dec.value
        else:
            bodyCoordinates=SkyCoord.from_name(self.name,frame='icrs')
            return bodyCoordinates.dec.value

    def SHAAt(self,Y,M,D,h,m,s):
        time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
        if self.type=="Star":
            bodyCoordinates=SkyCoord.from_name(self.name,frame='icrs')
            SHA=360.0-bodyCoordinates.ra.value
            return SHA
        else:
            return 0

    def SDAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            D=Distance(body.distance, unit=u.km).value
            d=celestialObjectDiameters[self.name]
            return degrees(atan(d/(2*D)))                        
        else:
            return 0

    def HPAt(self,Y,M,D,h,m,s):
        if not self.type=="Star":
            time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            D=Distance(body.distance, unit=u.km).value
            return degrees(atan(Rearth/D))
        else:
            return 0
