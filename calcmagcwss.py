#calculate magnetic correction for MSFS, using screensextant

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating magnetic correction for MSFS 2004, from time and celestial object position, using screensextant.")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
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

screenSextantConfigFile=open("Screen sextant.cfg")
screenSextantConfig = json.loads(screenSextantConfigFile.read())
screenSextantConfigFile.close()

screenSextantQuestions = [
    {
        "type":"input",
        "name":"Direction of view",
        "message":"Current direction of view:",
        "default":str(screenSextantConfig["Direction of view"])
    },
    {
        "type":"input",
        "name":"x",
        "message":"Horizontal coordinate on screen (x):",
        "default":str(screenSextantConfig["x"])
    },
    {
        "type":"input",
        "name":"y",
        "message":"Vertical coordinate on screen (y):",
        "default":str(screenSextantConfig["y"])
    },
    {
        "type":"confirm",
        "name":"Measured in pixels",
        "message":"Coordinates measured in pixels? (If \"No\" than in mm)",
        "default":str(screenSextantConfig["Measured in pixels"])
    },
    {
        "type":"list",
        "name":"Zoom level",
        "message":"Current zoom level:",
        "choices":["0.5","0.75"],
        "default":str(screenSextantConfig["Zoom level"])
    }
]

screenSextantAnswers = prompt(screenSextantQuestions)

screenSextantConfig["x"]=screenSextantAnswers["x"]
screenSextantConfig["y"]=screenSextantAnswers["y"]
screenSextantConfig["Direction of view"]=screenSextantAnswers["Direction of view"]
screenSextantConfig["Measured in pixels"]=screenSextantAnswers["Measured in pixels"]
screenSextantConfig["Zoom level"]=screenSextantAnswers["Zoom level"]

screenSextantConfigFile=open("Screen sextant.cfg","w")
screenSextantConfigFile.write(json.dumps(screenSextantConfig, indent=2))
screenSextantConfigFile.close()

import screensextant
import starcompass

mccConfigFile=open("Magnetic compass correction.cfg")
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
mccConfig["Azimuth from HDG"]=angle.ToJSONCompatible(angle.ToString(screensextant.ZfHDG))
mccConfig["Azimuth from north"]=angle.ToJSONCompatible(angle.ToString(starcompass.ZfN))

mccConfigFile=open("Magnetic compass correction.cfg", "w")
mccConfigFile.write(json.dumps(mccConfig, indent=2))
mccConfigFile.close()

import magcorrection

print("")
print("NB! [True HDG] = [magnetic HDG] + [correction for magnetic compass]")
