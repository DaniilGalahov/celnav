#navigation algorithms
import json
import timeprocessor
import almanac
import angle
import math
from trigonometry import sin, cos, tg, arcsin, arctg

from astropy.time import Time

class Observation:
    def __init__(self, configFileName):
        configFile=open(configFileName)
        self.config = json.loads(configFile.read())
        self.CalculateIntercept()

    def CalculateIntercept(self):
        self.astropyTimeString=time=timeprocessor.ToAstropyTimeString(self.config["Date"], self.config["Time"])
        celestialObject = almanac.GetCelestialObject(self.config["Celestial object"])
        
        self.Be=Be=angle.ToDecimal(self.config["Be"]) #self.Be required in other class methods
        self.Le=Le=angle.ToDecimal(self.config["Le"]) #same with Be

        h=self.config["Altitude"]
        
        Hs=angle.ToDecimal(self.config["Hs"]) #for MSFS must be measured by upper bound of sun/moon

        #here must be instrument correction

        Dip=0.0293*math.sqrt(h) #height correction
        H=Hs-Dip

        #here must be calculated refraction correction, but in MSFS it's not simulated correctly
        #here must be oblateness correction

        HP=celestialObject.HPAt(time)
        P=HP*cos(H)

        SD=celestialObject.SDAt(time)

        Ho=H+P+SD

        if not celestialObject.type=="Star":
            GHA=celestialObject.GHAAt(time)
            Dec=celestialObject.DecAt(time)
        else:
            GHAAries=almanac.GHAOfAriesAt(time)
            SHA=celestialObject.SHAAt(time)
            Dec=celestialObject.DecAt(time)
            GHA=GHAAries+SHA

        LHA=GHA+Le

        Hc=arcsin((sin(Be)*sin(Dec))+(cos(Be)*cos(Dec)*cos(LHA)))
        self.p=Ho-Hc

        self.Z=angle.Normalize(arctg(sin(LHA)/((sin(Be)*cos(LHA))-(cos(Be)*tg(Dec)))))

    @property
    def distance(self):
        return self.p*60.0*cos(self.Be)

    @property
    def time(self):
        return Time(self.astropyTimeString).to_value("unix")
