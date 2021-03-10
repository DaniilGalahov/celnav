#Alternative almanac based on astropy
from astropy.time import Time
from astropy.coordinates import Angle
from astropy.coordinates import solar_system_ephemeris, EarthLocation, SkyCoord, Distance
from astropy.coordinates import get_body
from astropy import units as u
import angle
from trigonometry import sin, cos, tg, arcsin, arctg

navigationPlanets=["Venus",
                   "Mars",
                   "Jupiter",
                   "Saturn"]
navigationStars=["Acamar",
                 "Achernar",
                 "Acrux",
                 "Adhara",
                 "Albireo",
                 "Aldebaran",
                 "Alioth",
                 "Alkaid",
                 "Al Na-ir",
                 "Alnilam",
                 "Alphard",
                 "Alphecca",
                 "Alpheratz",
                 "Altair",
                 "Ankaa",
                 "Antares",
                 "Arcturus",
                 "Atria",
                 "Avior",
                 "Bellatrix",
                 "Betelgeuse",
                 "Canopus",
                 "Capella",
                 "Castor",
                 "Deneb",
                 "Denebola",
                 "Diphda",
                 "Dubhe",
                 "Elnath",
                 "Eltanin",
                 "Enif",
                 "Fomalhaut",
                 "Gacrux",
                 "Gienah",
                 "Hadar",
                 "Hamal",
                 "Kochab",
                 "Markab",
                 "Menkar",
                 "Menkent",
                 "Miaplacidus",
                 "Mirfak",
                 "Nunki",
                 "Peacock",
                 "Polaris",
                 "Pollux",
                 "Procyon",
                 "Rasalhague",
                 "Regulus",
                 "Rigel",
                 "Sabik",
                 "Schedar",
                 "Shaula",
                 "Sirius",
                 "Spica",
                 "Suhail",
                 "Vega",
                 "Zuben-ubi"]

celestialObjectDiameters = { "Sun":1392700.0,
                             "Moon":3474.2,
                             "Venus":12104.0,
                             "Mars":6779.0,
                             "Jupiter":139820.0,
                             "Saturn":116460.0}
                             

ephemeris='builtin' #can be 'jpl' or 'de432s', but even in this case we have difference with Omar Reis about +14.5' in GHA and about -7' in Dec

def GHAOfAriesAt(time): #time must be GMT
    time = Time(time)
    siderealTime = time.sidereal_time('apparent', 'greenwich')
    return Angle(siderealTime).deg

class CelestialObject:
    def __init__(self, name): #name of celestial object must start from capital letter
        self.name=name
        
        self.type=None        
        if self.name=="Sun":
            self.type="Sun"
        elif self.name=="Moon":
            self.type="Moon"
        elif self.name in navigationPlanets:
            self.type="Planet"
        elif self.name in navigationStars:
            self.type="Star"
        
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

def GetCelestialObject(name):
    return CelestialObject(name)

#time="2021-03-10 00:00"
#print(angle.ToString(GHAOfAriesAt(time)))
#c=CelestialObject("Mars")
#print(angle.ToString(c.GHAAt(time)))
#print(angle.ToLatitude(c.DecAt(time)))
#print(angle.ToString(c.SHAAt(time)))
#print(angle.ToString(c.SDAt(time)))
#print(angle.ToString(c.HPAt(time)))
