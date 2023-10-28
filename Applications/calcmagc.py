#calculate magnetic correction

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating magnetic correction from time and celestial object position.")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
print("For static measurements with compass use current magnetic HDG 0.0*")
print("")

starCompassConfigFile=open("Star compass.cfg")
starCompassConfig = json.loads(starCompassConfigFile.read())
starCompassConfigFile.close()

starCompassQuestions = [
    {
        "type":"input",
        "name":"Date",
        "message":"Current date:",
        "default":str(starCompassConfig["Date"])
    },
    {
        "type":"input",
        "name":"Time",
        "message":"Measurement time (GMT):",
        "default":str(starCompassConfig["Time"])
    },
    {
        "type":"input",
        "name":"Celestial object",
        "message":"Observed celestial object:",
        "default":str(starCompassConfig["Celestial object"])
    },
    {
        "type":"input",
        "name":"Latitude",
        "message":"Est. observer latitude:",
        "default":str(starCompassConfig["Latitude"])
    },
    {
        "type":"input",
        "name":"Longtitude",
        "message":"Est. observer longtitude:",
        "default":str(starCompassConfig["Longtitude"])
    }
]

starCompassAnswers = prompt(starCompassQuestions)

starCompassConfig["Date"]=starCompassAnswers["Date"]
starCompassConfig["Time"]=starCompassAnswers["Time"]
starCompassConfig["Celestial object"]=starCompassAnswers["Celestial object"]
starCompassConfig["Latitude"]=starCompassAnswers["Latitude"]
starCompassConfig["Longtitude"]=starCompassAnswers["Longtitude"]

starCompassConfigFile=open("Star compass.cfg","w")
starCompassConfigFile.write(json.dumps(starCompassConfig, indent=2))
starCompassConfigFile.close()

celestialObjectQuestions=[
    {
        "type":"input",
        "name":"Azimuth from HDG",
        "message":"Azimuth from HDG to celestial object (0-360 deg, CW):",
        "default":str(0.0),
        "filter": lambda value: angle.ToJSONCompatible(angle.ToString(angle.ToDecimal(value)))
    }
]

celestialObjectAnswers = prompt(celestialObjectQuestions)

import starcompass

mccConfigFile=open("Mag correction.cfg")
mccConfig = json.loads(mccConfigFile.read())
mccConfigFile.close()

mccQuestions=[
    {
        "type":"input",
        "name":"Magnetic HDG",
        "message":"Current magnetic HDG (0-360 decimal deg, CW):",
        "default":str(round(angle.ToDecimal(mccConfig["Magnetic HDG"]),1)),
        "filter":lambda value:angle.ToJSONCompatible(angle.ToString(angle.ToDecimal(value)))
    }
]

mccAnswers = prompt(mccQuestions)

mccConfig["Magnetic HDG"]=mccAnswers["Magnetic HDG"]
mccConfig["Azimuth from HDG"]=celestialObjectAnswers["Azimuth from HDG"]
mccConfig["Azimuth from north"]=angle.ToJSONCompatible(angle.ToString(starcompass.ZfN))

mccConfigFile=open("Mag correction.cfg", "w")
mccConfigFile.write(json.dumps(mccConfig, indent=2))
mccConfigFile.close()

import magcorrection
input("Input any symbol to exit...")
