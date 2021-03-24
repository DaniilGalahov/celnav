#calculate angle from star/sun to north
import json
import almanac
import timeprocessor
import angle


configFile=open("Star compass.cfg")
config = json.loads(configFile.read())
configFile.close()

time=timeprocessor.ToAstropyTimeString(config["Date"], config["Time"])
celestialObject = almanac.GetCelestialObject(config["Celestial object"])
L=angle.ToDecimal(config["Longtitude"])
hemisphere=config["Hemisphere"]

if not celestialObject.type=="Star":
    GHA=celestialObject.GHAAt(time)
    LHA=GHA+L
else:    
    GHAAries=almanac.GHAOfAriesAt(time)
    SHA=celestialObject.SHAAt(time)
    LHA=GHAAries+SHA+L
    

c=180
if(hemisphere!="N"):
    c=0

StNA=LHA+c

print("Angle from star to north, CC: "+angle.ToString(StNA)) #angle always counter-clockwise
