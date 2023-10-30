#Celestial object implementation for working with astropy
from astropy.time import Time
from astropy.coordinates import Angle
from astropy.coordinates import solar_system_ephemeris, EarthLocation, SkyCoord, Distance
from astropy.coordinates import get_body
from astropy import units as u

from celestialobject import navigationPlanetNames, celestialObjectDiameters, CelestialObject
from catalog import navigationStarNames
from trigonometry import arctg

ephemeris='builtin' #can be 'jpl' or 'de432s', but even in this case we have difference with Omar Reis about +14.5' in GHA and about -7' in Dec

def GHAOfAriesAt(time): #time must be GMT
    time = Time(time)
    siderealTime = time.sidereal_time('apparent', 'greenwich')
    return Angle(siderealTime).deg

class CelestialObjectFromAstroPy(CelestialObject):
    def GHAAt(self, time):
        time=Time(time)
        if not self.type=="Star":            
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            GHA=GHAOfAriesAt(time)-body.ra.value       
            return GHA
        else:
            return 0

    def DecAt(self, time):
        time=Time(time)
        if not self.type=="Star":            
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            return body.dec.value
        else:
            bodyCoordinates=SkyCoord.from_name(self.name,frame='icrs')
            return bodyCoordinates.dec.value

    def SHAAt(self, time):
        time=Time(time)
        if self.type=="Star":
            bodyCoordinates=SkyCoord.from_name(self.name,frame='icrs')
            SHA=360.0-bodyCoordinates.ra.value
            return SHA
        else:
            return 0

    def SDAt(self, time):
        if not self.type=="Star":
            time=Time(time)
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            D=Distance(body.distance, unit=u.km).value
            d=celestialObjectDiameters[self.name]
            return arctg(d/(2*D))                        
        else:
            return 0

    def HPAt(self, time):
        if not self.type=="Star":
            time=Time(time)
            location=EarthLocation.of_site('greenwich')
            with solar_system_ephemeris.set(ephemeris):
                body=get_body(self.name, time, location)
            L=6371.0 #radius of Earth, km
            D=Distance(body.distance, unit=u.km).value
            return arctg(L/D)
        else:
            return 0
