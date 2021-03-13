#calculate correction for magnetic compass
#(Not magnetic declination! [Correction]=[-1]*[magnetic declination])
import json
import angle

configFile=open("Magnetic compass correction.cfg")
config = json.loads(configFile.read())

HDG = angle.ToDecimal(config["Magnetic HDG"])
ZfHDG = angle.ToDecimal(config["Azimuth from HDG"])
StNA = angle.ToDecimal(config["Angle from star to north"])

correction=HDG+ZfHDG-StNA

print("Correction for magnetic compass: "+str(correction))
print("Magnetic deviation: "+str(-correction))
