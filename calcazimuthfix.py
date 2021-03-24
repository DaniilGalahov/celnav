#calculate azimuth fix

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating observer position from azimuths towards two known objects.")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
print("")


configFile=open("Azimuth fix.cfg")
config = json.loads(configFile.read())
configFile.close()

def GetAnswersAbout(knownObject):
    objectQuestions = [
        {
            "type":"input",
            "name":"Latitude",
            "message":"Latitude (dd*mm.mm' N/S):",
            "default":str(knownObject["Latitude"])
        },
        {
            "type":"input",
            "name":"Longtitude",
            "message":"Longtitude (dd*mm.mm' E/W):",
            "default":str(knownObject["Longtitude"])
        },
        {
            "type":"input",
            "name":"Bearing",
            "message":"Bearing (0-360 deg, CC):",
            "default":str(round(angle.ToDecimal(knownObject["Bearing"]),1)),
            "filter":lambda value:str(angle.ToDecimal(value))
        }
    ]

    return prompt(objectQuestions)

print("Object 1:")
object1Answers=GetAnswersAbout(config["Object1"])
print("Object 2:")
object2Answers=GetAnswersAbout(config["Object2"])

config["Object1"]["Bearing"]=object1Answers["Bearing"]
config["Object1"]["Latitude"]=object1Answers["Latitude"]
config["Object1"]["Longtitude"]=object1Answers["Longtitude"]

config["Object2"]["Bearing"]=object2Answers["Bearing"]
config["Object2"]["Latitude"]=object2Answers["Latitude"]
config["Object2"]["Longtitude"]=object2Answers["Longtitude"]

configFile=open("Azimuth fix.cfg","w")
configFile.write(json.dumps(config, indent=2))
configFile.close()

print("")
print("Observer position:")
import azimuthfix
