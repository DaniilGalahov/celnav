#almanac data source for using in other navigation scripts
import json
import timeprocessor
import angle

configFile=open("Almanac.cfg")
config = json.loads(configFile.read())

def CalculateRelativeTime(absoluteTime):
    absoluteTime=timeprocessor.ToSeconds(absoluteTime)
    if not period.Includes(absoluteTime):
        print("Incorrect time")
        quit()
    else:
        return (absoluteTime-period.begin)/(period.end-period.begin)

def CalculateExactValueFor(relativeTime, value1, value2):
    return value1 + ((value2-value1)*relativeTime)

class Period:
    def __init__(self,period):
        self.begin=timeprocessor.ToSeconds(period["Begin"])
        self.end=timeprocessor.ToSeconds(period["End"])

    def Includes(self,time):
        time=timeprocessor.ToSeconds(time)
        if time>=self.begin and time<=self.end:
            return True
        else:
            return False

class Aries:
    def __init__ (self,aries):
        self.atBegin=angle.ToDecimal(aries["AtBegin"])
        self.atEnd=angle.ToDecimal(aries["AtEnd"])

    def At(self, time):
        return CalculateExactValueFor(CalculateRelativeTime(time), self.atBegin, self.atEnd)

class CelestialObject:
    def __init__(self, name):
        self.name=name

    @property
    def type(self):
        return celestialObjects[self.name]["Type"]

    def GHAAt(self, time):        
        return CalculateExactValueFor(CalculateRelativeTime(time), angle.ToDecimal(self.AtBegin("GHA")), angle.ToDecimal(self.AtEnd("GHA")))

    def DecAt(self, time):        
        return CalculateExactValueFor(CalculateRelativeTime(time), angle.ToDecimal(self.AtBegin("Dec")), angle.ToDecimal(self.AtEnd("Dec")))

    @property
    def Dec(self):
        return angle.ToDecimal(celestialObjects[self.name]["Dec"])

    @property
    def SD(self):
        return angle.ToDecimal(celestialObjects[self.name]["SD"])

    @property
    def HP(self):
        return angle.ToDecimal(celestialObjects[self.name]["HP"])

    def HPAt(self, time):        
        return CalculateExactValueFor(CalculateRelativeTime(time), angle.ToDecimal(self.AtBegin("HP")), angle.ToDecimal(self.AtEnd("HP")))

    @property
    def SHA(self):
        return angle.ToDecimal(celestialObjects[self.name]["SHA"])

    def AtBegin(self, parameter):
        return celestialObjects[self.name]["AtBegin"][parameter]

    def AtEnd(self, parameter):
        return celestialObjects[self.name]["AtEnd"][parameter]


date=config["Date"]
period=Period(config["Period"])
aries=Aries(config["Aries"])
celestialObjects=config["Celestial objects"]

def IsCorrectFor(date, time):
    if date==date and period.Includes(time):
        return True
    else:
        return False

def GetCelestialObject(name):
    return CelestialObject(name)   



