#interface to astronomical almanach systems - based on AstroPy or local catalog and ephemerides
from external.modules import *

from celestialobject import CelestialObject
from coapy import CelestialObjectFromAstroPy
from coloc import CelestialObjectFromLocalCatalog

config=configparser.ConfigParser()
configFilePath=os.path.join(os.path.dirname(__file__),'config.ini')
config.read(configFilePath)
source=int(config['MAIN']["AlmanacEngine"])

if source==0:
    from coapy import GHAOfAriesAt
elif source==1:
    from coloc import GHAOfAriesAt

def GetCelestialObject(name):
    if source==0:
        return CelestialObjectFromAstroPy(name)
    elif source==1:
        return CelestialObjectFromLocalCatalog(name)
