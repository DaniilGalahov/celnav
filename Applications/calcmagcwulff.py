#calculate magnetic correction for MSFS, using wulff

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating magnetic correction for MSFS 2004, from time and celestial object position, using wulff.")
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

wulffConfigFile=open("Wulff.cfg")
wulffConfig = json.loads(wulffConfigFile.read())
wulffConfigFile.close()

wulffQuestions = [
    {
        "type":"input",
        "name":"Direction of view",
        "message":"Current direction of view:",
        "default":str(wulffConfig["Direction of view"])
    },
    {
        "type":"input",
        "name":"Z",
        "message":"Azimuth of object on Wulff net:",
        "default":str(wulffConfig["Z"])
    },
    {
        "type":"input",
        "name":"H",
        "message":"Height of object on Wulff net:",
        "default":str(wulffConfig["H"])
    }
]

wulffAnswers = prompt(wulffQuestions)

wulffConfig["Direction of view"]=wulffAnswers["Direction of view"]
wulffConfig["Z"]=wulffAnswers["Z"]
wulffConfig["H"]=wulffAnswers["H"]

wulffConfigFile=open("Wulff.cfg","w")
wulffConfigFile.write(json.dumps(wulffConfig, indent=2))
wulffConfigFile.close()

import wulff
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
mccConfig["Azimuth from HDG"]=angle.ToJSONCompatible(angle.ToString(wulff.ZfHDG))
mccConfig["Azimuth from north"]=angle.ToJSONCompatible(angle.ToString(starcompass.ZfN))

mccConfigFile=open("Mag correction.cfg", "w")
mccConfigFile.write(json.dumps(mccConfig, indent=2))
mccConfigFile.close()

import magcorrection

print("")
print("NB! [True HDG] = [magnetic HDG] + [correction for magnetic compass]")
input("Input any symbol to exit...")
