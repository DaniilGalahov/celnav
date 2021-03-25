#simple navigational calculator
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json

print("Calculate waypoints on orthodromy from travelled distance, desired speed and environment parameters.")
print("")

def CalculateHeadingToNextWaypoint():
    routeConfigFile=open("Route.cfg")
    routeConfig = json.loads(routeConfigFile.read())
    routeConfigFile.close()

    nextWaypointQuestions=[
            {
                "type":"confirm",
                "name":"Update travelled distance",
                "message":"Update travelled distance? (DO NOT update in you are on first WPT or recalculating HDG!)",
                "default":True
            },
            {
                "type":"input",
                "name":"Distance to next waypoint, nmi",
                "message":"Distance to next waypoint (nmi):",
                "default":str(routeConfig["Distance to next waypoint, nmi"])
            },
            {
                "type":"input",
                "name":"Desired speed, kts",
                "message":"Desired speed (kts):",
                "default":str(routeConfig["Desired speed, kts"])
            },
            {
                "type":"input",
                "name":"Magnetic compass correction",
                "message":"Magnetic compass correction:",
                "default":str(routeConfig["Magnetic compass correction"])
            },
            {
                "type":"input",
                "name":"Wind direction",
                "message":"Wind direction:",
                "default":str(routeConfig["Wind"]["Direction"])
            },
            {
                "type":"input",
                "name":"Wind speed",
                "message":"Wind speed (kts):",
                "default":str(routeConfig["Wind"]["Speed, kts"])
            }
        ]
    nextWaypointAnswers=prompt(nextWaypointQuestions)

    if nextWaypointAnswers["Update travelled distance"]:
        routeConfig["Distance travelled, nmi"]=str(float(routeConfig["Distance travelled, nmi"])+float(routeConfig["Distance to next waypoint, nmi"]))

    routeConfig["Distance to next waypoint, nmi"]=nextWaypointAnswers["Distance to next waypoint, nmi"]
    routeConfig["Desired speed, kts"]=nextWaypointAnswers["Desired speed, kts"]
    routeConfig["Magnetic compass correction"]=nextWaypointAnswers["Magnetic compass correction"]
    routeConfig["Wind"]["Direction"]=nextWaypointAnswers["Wind direction"]
    routeConfig["Wind"]["Speed, kts"]=nextWaypointAnswers["Wind speed"]

    routeConfigFile=open("Route.cfg","w")
    routeConfigFile.write(json.dumps(routeConfig, indent=2))
    routeConfigFile.close()

    import gcnm

def GetAnswersAbout(position):
    positionQuestions = [
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

    return prompt(positionQuestions)

def SetupRoute():
    routeConfigFile=open("Route.cfg")
    routeConfig = json.loads(routeConfigFile.read())
    routeConfigFile.close()

    print("Setup start position:")
    startPositionAnswers=GetAnswersAbout(routeConfig["Start"])
    routeConfig["Start"]["Latitude"]=startPositionAnswers["Latitude"]
    routeConfig["Start"]["Longtitude"]=startPositionAnswers["Longtitude"]

    print("\nSetup destination position:")
    destinationPositionAnswers=GetAnswersAbout(routeConfig["Destination"])
    routeConfig["Destination"]["Latitude"]=destinationPositionAnswers["Latitude"]
    routeConfig["Destination"]["Longtitude"]=destinationPositionAnswers["Longtitude"]

    routeConfig["Distance travelled, nmi"]=0.0

    routeConfigFile=open("Route.cfg","w")
    routeConfigFile.write(json.dumps(routeConfig, indent=2))
    routeConfigFile.close()

    print("\nRoute successfully configured.")

modeQuestion = [
        {
            "type":"list",
            "name":"Mode",
            "message":"Select mode:",
            "choices": [
                "Calculate HDG to next WPT",
                "Setup route",
                "Quit"
                ]            
        }
    ]

modeAnswer=prompt(modeQuestion)

if modeAnswer["Mode"]=="Calculate HDG to next WPT":
    CalculateHeadingToNextWaypoint()
elif modeAnswer["Mode"]=="Setup route":
    SetupRoute()
