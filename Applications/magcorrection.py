#calculate correction for magnetic compass
#(Not magnetic declination! [Correction]=[-1]*[magnetic declination])
import json
import angle

configFile=open("Mag correction.cfg")
config = json.loads(configFile.read())
configFile.close()

HDG = angle.ToDecimal(config["Magnetic HDG"])
ZfHDG = angle.ToDecimal(config["Azimuth from HDG"])
ZfN = angle.ToDecimal(config["Azimuth from north"])

correction=round(angle.ToSigned180(HDG+ZfHDG-ZfN),1)

print("Correction for magnetic compass: "+str(correction))
print("(Magnetic deviation: "+str(-correction)+")")
