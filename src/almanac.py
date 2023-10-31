#interface to astronomical almanach systems - based on AstroPy or local catalog and ephemerides
from celestialobject import CelestialObject
from coapy import CelestialObjectFromAstroPy
from coloc import CelestialObjectFromLocalCatalog

source=1 #0 - AstroPy, 1 - local catalog and ephemeris based on hipparchos, simbad and Vallado code

if source==0:
    from coapy import GHAOfAriesAt
elif source==1:
    from coloc import GHAOfAriesAt

def GetCelestialObject(name):
    if source==0:
        return CelestialObjectFromAstroPy(name)
    elif source==1:
        return CelestialObjectFromLocalCatalog(name)
