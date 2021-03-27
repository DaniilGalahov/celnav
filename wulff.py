#calculate ZfHDG and H from readings from Wulff stereonet
import json
import angle

configFile=open("Wulff.cfg")
config = json.loads(configFile.read())
configFile.close()

viewDir=float(config["Direction of view"])
Z=float(config["Z"])
H=float(config["H"])

ZfHDG=viewDir+Z

print("Azimuth from HDG: "+angle.ToString(ZfHDG))
print("Height: "+angle.ToString(H))
