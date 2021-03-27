#calculate angle from star/sun to north
#Based on description in HANDBOOK OF MAGNETICCOMPASS ADJUSTMENT
import json
import almanac
import timeprocessor
import angle
from trigonometry import sin, cos, tg, atan2


configFile=open("Star compass.cfg")
config = json.loads(configFile.read())
configFile.close()

time=timeprocessor.ToAstropyTimeString(config["Date"], config["Time"])
celestialObject = almanac.GetCelestialObject(config["Celestial object"])
B=angle.ToDecimal(config["Latitude"])
L=angle.ToDecimal(config["Longtitude"])

if not celestialObject.type=="Star":
    GHA=celestialObject.GHAAt(time)
    LHA=GHA+L
else:    
    GHAAries=almanac.GHAOfAriesAt(time)
    SHA=celestialObject.SHAAt(time)
    LHA=GHAAries+SHA+L

#Commented algorithm (my original variant) also worked well!
#c=180
#if(hemisphere!="N"):
#    c=0
#
#ZfN=LHA+c

Dec=celestialObject.DecAt(time)

ZfN=360.0 - atan2( sin(LHA), (cos(B)*tg(Dec))-(sin(B)*cos(LHA)))

print("North azimuth of star: "+angle.ToString(ZfN))
