#calculate magnetic correction for MSFS, using wulff

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating magnetic correction for MSFS 2004, from IGRF")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
print("")

configFile=open("Mag correction from IGRF.cfg")
config = json.loads(configFile.read())
configFile.close()

questions=[
        {
            "type":"input",
            "name":"Latitude",
            "message":"Latitude (dd*mm.mm' N/S):",
            "default":str(config["Latitude"])
        },
        {
            "type":"input",
            "name":"Longtitude",
            "message":"Longtitude (dd*mm.mm' E/W):",
            "default":str(config["Longtitude"])
        },
        {
            "type":"input",
            "name":"Altitude",
            "message":"Altitude (m):",
            "default":str(config["Altitude"])
        },
        {
            "type":"input",
            "name":"Year",
            "message":"Year (YYYY, 1982 for MSFS2004):",
            "default":str(config["Year"])
        }
]

answers = prompt(questions)

config["Latitude"]=answers["Latitude"]
config["Longtitude"]=answers["Longtitude"]
config["Altitude"]=answers["Altitude"]
config["Year"]=answers["Year"]

configFile=open("Mag correction from IGRF.cfg", "w")
configFile.write(json.dumps(config, indent=2))
configFile.close()

import magcorrectionigrf

print("")
print("NB! [True HDG] = [magnetic HDG] + [correction for magnetic compass]")
input("Input any symbol to exit...")
