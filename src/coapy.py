#Celestial object implementation for working with astropy
from external.math import degrees, atan, vector, magnitude
from external.astro import Time, get_body, solar_system_ephemeris, Angle, EarthLocation, SkyCoord, Distance, u
from celestialobject import navigationPlanetNames, celestialObjectDiameters, Rearth, CelestialObject
from catalog import navigationStarNames
from timeprocessor import YMDhmsToAPyTime
from angle import Normalize

ephemeris='builtin' #can be 'jpl' or 'de432s', but even in this case we have difference with Omar Reis about +14.5' in GHA and about -7' in Dec

def GHAOfAriesAt(Y,M,D,h,m,s): #time must be GMT
    time = Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
    siderealTime = time.sidereal_time('mean', 'greenwich', 'IAU2006') #must be mean!
    return Normalize(Angle(siderealTime).deg) #must be normalized to match values from Nautical Almanac

class CelestialObjectFromAstroPy(CelestialObject):
    def VectorAt(self,Y,M,D,h,m,s):
        time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
        if not self.type=="Star":            
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time)
                body.representation_type='cartesian'
            return vector([body.x.to(u.km).value,body.y.to(u.km).value,body.z.to(u.km).value])
        else:
            bodyCoordinates=SkyCoord.from_name(self.name,frame='icrs')
            bodyCoordinates.representation_type='cartesian'
            vector_r=vector([bodyCoordinates.x.value,bodyCoordinates.y.value,bodyCoordinates.z.value])
            return vector_r/magnitude(vector_r)

    def GHAAt(self,Y,M,D,h,m,s):
        time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
        if not self.type=="Star":            
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            GHA=Normalize(GHAOfAriesAt(Y,M,D,h,m,s)-body.ra.value-self.SDAt(Y,M,D,h,m,s)-self.HPAt(Y,M,D,h,m,s)) #astropy getting in count SD and HP of celestial body, so we removing this to get right value
            return GHA
        else:
            return 0

    def DecAt(self,Y,M,D,h,m,s):
        time=Time(YMDhmsToAPyTime(Y,M,D,h,m,s))
        if not self.type=="Star":            
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            return body.dec.value+self.SDAt(Y,M,D,h,m,s)+self.HPAt(Y,M,D,h,m,s)  #astropy getting in count SD and HP of celestial body, so here we adding this to get right value
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
