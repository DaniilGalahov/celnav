#calculate angle from star/sun to north
import json
import almanac
import timeprocessor
import angle


configFile=open("Star compass.cfg")
config = json.loads(configFile.read())

time=timeprocessor.ToSeconds(config["Time"]) #because we need time not only in checking almanac validity, but also in calculations later

if not almanac.IsCorrectFor(config["Date"],time):
    print("Almanac data incorrect for required date/time.")
    quit()

celestialObject = almanac.GetCelestialObject(config["Celestial object"])
L=angle.ToDecimal(config["Longtitude"])
hemisphere=config["Hemisphere"]

if celestialObject.type!="Star":
    GHA=celestialObject.GHAAt(time)
    LHA=GHA+L
else:    
    GHAAries=almanac.aries.At(time)
    SHA=celestialObject.SHA
    LHA=GHAAries+SHA+L

c=180
if(hemisphere!="N"):
    c=0

StNA=LHA+c

print("Angle from star to north, CC: "+angle.ToString(StNA)) #angle always counter-clockwise
