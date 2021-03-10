#calculate geographical point of star/sun
import json
import timeprocessor
import almanac
import angle


configFile=open("StarGP.cfg")
config = json.loads(configFile.read())

time=timeprocessor.ToAstropyTimeString(config["Date"], config["Time"])
celestialObject = almanac.GetCelestialObject(config["Celestial object"])

if not celestialObject.type=="Star":
    GHA=celestialObject.GHAAt(time)
    Dec=celestialObject.DecAt(time)
else:
    GHAAries=almanac.GHAOfAriesAt(time)
    SHA=celestialObject.SHAAt(time)
    Dec=celestialObject.DecAt(time)
    GHA=GHAAries+SHA

L=Dec
B=angle.Normalize(360.0-GHA)

print(angle.ToLatitude(L))
print(angle.ToLongtitude(B))
