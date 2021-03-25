#calculate angles of celestial object in MSFS with screensextant
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating angles of celestial object in MSFS 2004.")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
print("")

configFile=open("Screen sextant.cfg")
config = json.loads(configFile.read())
configFile.close()

questions = [
    {
        "type":"input",
        "name":"Direction of view",
        "message":"Current direction of view:",
        "default":str(config["Direction of view"])
    },
    {
        "type":"input",
        "name":"x",
        "message":"Horizontal coordinate on screen (x):",
        "default":str(config["x"])
    },
    {
        "type":"input",
        "name":"y",
        "message":"Vertical coordinate on screen (y):",
        "default":str(config["y"])
    },
    {
        "type":"confirm",
        "name":"Measured in pixels",
        "message":"Coordinates measured in pixels? (If \"No\" than in mm)",
        "default":str(config["Measured in pixels"])
    },
    {
        "type":"list",
        "name":"Zoom level",
        "message":"Current zoom level:",
        "choices":["0.5","0.75"],
        "default":str(config["Zoom level"])
    }
]

answers = prompt(questions)

config["x"]=answers["x"]
config["y"]=answers["y"]
config["Direction of view"]=answers["Direction of view"]
config["Measured in pixels"]=answers["Measured in pixels"]
config["Zoom level"]=answers["Zoom level"]

configFile=open("Screen sextant.cfg","w")
configFile.write(json.dumps(config, indent=2))
configFile.close()

import screensextant
