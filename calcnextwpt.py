#simple navigational calculator
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json

print("Calculate waypoints on orthodromy from travelled distance, desired speed and environment parameters.")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
print("")

def CalculateHeadingToNextWaypoint():
    configFile=open("Route.cfg")
    config = json.loads(configFile.read())
    configFile.close()

    questions=[
            {
                "type":"confirm",
                "name":"Update travelled distance",
                "message":"Update travelled distance with "+str(config["Distance to next waypoint, nmi"])+" nmi? (DO NOT update in you are on first WPT or recalculating HDG!)",
                "default":True
            },
            {
                "type":"input",
                "name":"Distance to next waypoint, nmi",
                "message":"Distance to next waypoint (nmi):",
                "default":str(config["Distance to next waypoint, nmi"])
            },
            {
                "type":"input",
                "name":"Desired speed, kts",
                "message":"Desired speed (kts):",
                "default":str(config["Desired speed, kts"])
            },
            {
                "type":"input",
                "name":"Magnetic compass correction",
                "message":"Magnetic compass correction:",
                "default":str(config["Magnetic compass correction"])
            },
            {
                "type":"input",
                "name":"Wind direction",
                "message":"Wind direction:",
                "default":str(config["Wind"]["Direction"])
            },
            {
                "type":"input",
                "name":"Wind speed",
                "message":"Wind speed (kts):",
                "default":str(config["Wind"]["Speed, kts"])
            }
        ]
    answers=prompt(questions)

    if answers["Update travelled distance"]:
        config["Distance travelled, nmi"]=str(float(config["Distance travelled, nmi"])+float(config["Distance to next waypoint, nmi"]))

    config["Distance to next waypoint, nmi"]=answers["Distance to next waypoint, nmi"]
    config["Desired speed, kts"]=answers["Desired speed, kts"]
    config["Magnetic compass correction"]=answers["Magnetic compass correction"]
    config["Wind"]["Direction"]=answers["Wind direction"]
    config["Wind"]["Speed, kts"]=answers["Wind speed"]

    configFile=open("Route.cfg","w")
    configFile.write(json.dumps(config, indent=2))
    configFile.close()

    import gcnm

def GetAnswersAbout(position):
    questions = [
        {
            "type":"input",
            "name":"Latitude",
            "message":"Latitude (dd*mm.mm' N/S):",
            "default":str(position["Latitude"])
        },
        {
            "type":"input",
            "name":"Longtitude",
            "message":"Longtitude (dd*mm.mm' E/W):",
            "default":str(position["Longtitude"])
        }
    ]

    return prompt(questions)

def SetRoute():
    configFile=open("Route.cfg")
    config = json.loads(configFile.read())
    configFile.close()

    print("Set start position:")
    startPositionAnswers=GetAnswersAbout(config["Start"])
    config["Start"]["Latitude"]=startPositionAnswers["Latitude"]
    config["Start"]["Longtitude"]=startPositionAnswers["Longtitude"]

    print("\nSet destination position:")
    destinationPositionAnswers=GetAnswersAbout(config["Destination"])
    config["Destination"]["Latitude"]=destinationPositionAnswers["Latitude"]
    config["Destination"]["Longtitude"]=destinationPositionAnswers["Longtitude"]

    config["Distance travelled, nmi"]=0.0

    configFile=open("Route.cfg","w")
    configFile.write(json.dumps(config, indent=2))
    configFile.close()

    print("\nRoute successfully configured.")


modeQuestion = [
        {
            "type":"list",
            "name":"Mode",
            "message":"Select mode:",
            "choices": [
                "Calculate HDG to next WPT",
                "Set route",
                "Quit"
                ]            
        }
    ]

modeAnswer=prompt(modeQuestion)

if modeAnswer["Mode"]=="Calculate HDG to next WPT":
    CalculateHeadingToNextWaypoint()
elif modeAnswer["Mode"]=="Set route":
    SetRoute()
