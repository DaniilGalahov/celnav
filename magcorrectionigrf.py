#get magC from IGRF13
import json
import angle
import pyIGRF

configFile=open("Mag correction from IGRF.cfg")
config = json.loads(configFile.read())
configFile.close()

B=angle.ToDecimal(config["Latitude"])
L=angle.ToDecimal(config["Longtitude"])
h=float(config["Altitude"])
year=int(config["Year"])

D,I,H,X,Y,Z,F=pyIGRF.igrf_value(B, L, h, year)

correction=round(angle.ToSigned180(D),1)

print("Correction for magnetic compass: "+str(correction))
print("(Magnetic deviation: "+str(-correction)+")")
