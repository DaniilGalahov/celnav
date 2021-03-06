#calculate geographical point of star/sun
import json
import timeprocessor
import almanac
import angle


configFile=open("StarGP.cfg")
config = json.loads(configFile.read())

time=timeprocessor.ToSeconds(config["Time"]) #must be GMT

if not almanac.IsCorrectFor(config["Date"],time):
    print("Almanac data incorrect for required date/time.")
    quit()

celestialObject = almanac.GetCelestialObject(config["Celestial object"])

if not celestialObject.type=="Star":
    Dec=celestialObject.DecAt(time)
    GHA=celestialObject.GHAAt(time)
else:
    Dec=celestialObject.Dec
    GHAAries=almanac.aries.At(time)
    SHA=celestialObject.SHA    
    GHA=GHAAries+SHA

L=Dec
B=angle.Normalize(360.0-GHA)

print(angle.ToLatitude(L))
print(angle.ToLongtitude(B))
