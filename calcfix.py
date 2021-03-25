#celestial navigation position fix calculator
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import angle

print("Calculating observer position from observed celestial objects positions")
print("")
print("NB! Replace degrees sign ('°') with '*' for compatibility with python json.")
print("")

def PrepareParameter(passed, loaded):
    parameter = {"Value":loaded,"Notification":""}
    if not passed is None:
        parameter["Value"]=passed
        parameter["Notification"]="(recieved from main script)"
    return parameter
    
def ConfigureObservation(fileName, *args, **kvargs):
    print("Configuring "+fileName+".")
    
    configFile=open(fileName)
    config = json.loads(configFile.read())
    configFile.close()

    date=kvargs.get("date", None)
    time=kvargs.get("time", None)
    celestialObject=kvargs.get("celestialObject", None)
    Be=kvargs.get("Be", None)
    Le=kvargs.get("Le", None)
    altitude=kvargs.get("altitude", None)
    temperature=kvargs.get("temperature", None)
    pressure=kvargs.get("pressure", None)

    date=PrepareParameter(date,config["Date"])
    time=PrepareParameter(time,config["Time"])
    celestialObject=PrepareParameter(celestialObject,config["Celestial object"])
    Be = PrepareParameter(Be,config["Be"])
    Le = PrepareParameter(Le,config["Le"])
    altitude = PrepareParameter(altitude,config["Altitude"])
    temperature = PrepareParameter(temperature,config["Temperature"])
    pressure = PrepareParameter(pressure,config["Pressure"])
    
    print("Each parameter is loaded from an observation file, unless otherwise source specified.\n")
    
    questions=[
            {
                "type":"input",
                "name":"Date",
                "message":"Date (DD.MM.YYYY) "+date["Notification"]+":",
                "default":str(date["Value"])
            },
            {
                "type":"input",
                "name":"Time",
                "message":"Time (GMT, HH:MM) "+time["Notification"]+":",
                "default":str(time["Value"])
            },
            {
                "type":"input",
                "name":"Celestial object",
                "message":"Celestial object "+celestialObject["Notification"]+":",
                "default":celestialObject["Value"]
            },
            {
                "type":"input",
                "name":"Be",
                "message":"Est. latitude (dd*mm.mm' N/S) "+Be["Notification"]+":",
                "default":str(Be["Value"])
            },
            {
                "type":"input",
                "name":"Le",
                "message":"Est. longtitude (dd*mm.mm' E/W) "+Le["Notification"]+":",
                "default":str(Le["Value"])
            },
            {
                "type":"input",
                "name":"Altitude",
                "message":"Altitude, m "+altitude["Notification"]+":",
                "default":str(altitude["Value"])
            },
            {
                "type":"input",
                "name":"Temperature",
                "message":"Temperature, °C "+temperature["Notification"]+":",
                "default":str(temperature["Value"])
            },
            {
                "type":"input",
                "name":"Pressure",
                "message":"Pressure, mbar/hPa "+pressure["Notification"]+":",
                "default":str(pressure["Value"])
            },
            {
                "type":"input",
                "name":"Hs",
                "message":"Measured height of object:",
                "default":config["Hs"],
                "filter":lambda value:angle.ToJSONCompatible(angle.ToString(angle.ToDecimal(value)))
            }
        ]

    answers=prompt(questions)

    config["Date"]=answers["Date"]
    config["Time"]=answers["Time"]
    config["Celestial object"]=answers["Celestial object"]
    config["Be"]=answers["Be"]
    config["Le"]=answers["Le"]
    config["Altitude"]=answers["Altitude"]
    config["Temperature"]=answers["Temperature"]
    config["Pressure"]=answers["Pressure"]
    config["Hs"]=answers["Hs"]
    
    configFile=open(fileName,"w")
    configFile.write(json.dumps(config, indent=2))
    configFile.close()

    print("\n"+fileName+" configured successfully.")

def Intercept():
    ConfigureObservation("Observation1.cfg")
    print("\nCalculating intercept...\n")
    import intercept

def OneObjectFix():
    print("Configuring common parameters.\n")

    positionConfigFile=open("Position.cfg")
    positionConfig = json.loads(positionConfigFile.read())
    positionConfigFile.close()
    
    configFile=open("One object fix.cfg")
    config = json.loads(configFile.read())
    configFile.close()

    questions=[
            {
                "type":"input",
                "name":"Be",
                "message":"Est. latitude (dd*mm.mm' N/S):",
                "default":str(positionConfig["Be"]),
                "filter":lambda value:angle.ToJSONCompatible(angle.ToLatitude(angle.ToDecimal(value)))
            },            
            {
                "type":"input",
                "name":"Le",
                "message":"Est. longtitude (dd*mm.mm' E/W):",
                "default":str(positionConfig["Le"]),
                "filter":lambda value:angle.ToJSONCompatible(angle.ToLongtitude(angle.ToDecimal(value)))
            },
            {
                "type":"input",
                "name":"Celestial object",
                "message":"Celestial object:",
                "default":config["Celestial object"]
            },
            {
                "type":"input",
                "name":"Ground speed, kts",
                "message":"Ground speed (kts):",
                "default":str(config["Ground speed, kts"])
            },
            {
                "type":"input",
                "name":"Heading",
                "message":"HDG:",
                "default":str(config["Heading"])
            }
        ]
    answers=prompt(questions)    

    config["Celestial object"]=answers["Celestial object"]
    config["Ground speed, kts"]=answers["Ground speed, kts"]
    config["Heading"]=answers["Heading"]

    positionConfig["Be"]=answers["Be"]
    positionConfig["Le"]=answers["Le"]

    configFile=open("One object fix.cfg","w")
    configFile.write(json.dumps(config, indent=2))
    configFile.close()

    positionConfigFile=open("Position.cfg", "w")
    positionConfigFile.write(json.dumps(positionConfig, indent=2))
    positionConfigFile.close()

    print("")
    ConfigureObservation("Observation1.cfg", celestialObject=config["Celestial object"], Be=positionConfig["Be"], Le=positionConfig["Le"])
    print("")
    ConfigureObservation("Observation2.cfg", celestialObject=config["Celestial object"], Be=positionConfig["Be"], Le=positionConfig["Le"])

    print("\nCalculating fix...\n")
    import oneobjectfix

def TwoObjectsFix():
    print("Configuring common parameters.\n")

    positionConfigFile=open("Position.cfg")
    positionConfig = json.loads(positionConfigFile.read())
    positionConfigFile.close()

    questions=[
            {
                "type":"input",
                "name":"Be",
                "message":"Est. latitude (dd*mm.mm' N/S):",
                "default":str(positionConfig["Be"]),
                "filter":lambda value:angle.ToJSONCompatible(angle.ToLatitude(angle.ToDecimal(value)))
            },            
            {
                "type":"input",
                "name":"Le",
                "message":"Est. longtitude (dd*mm.mm' E/W):",
                "default":str(positionConfig["Le"]),
                "filter":lambda value:angle.ToJSONCompatible(angle.ToLongtitude(angle.ToDecimal(value)))
            }
        ]
    answers=prompt(questions)

    print("")
    ConfigureObservation("Observation1.cfg", Be=positionConfig["Be"], Le=positionConfig["Le"])
    print("")
    ConfigureObservation("Observation2.cfg", Be=positionConfig["Be"], Le=positionConfig["Le"])
    
    print("\nCalculating fix...\n")
    import twoobjectsfix

def ThreeObjectsFix():
    print("Configuring common parameters.\n")

    positionConfigFile=open("Position.cfg")
    positionConfig = json.loads(positionConfigFile.read())
    positionConfigFile.close()

    questions=[
            {
                "type":"input",
                "name":"Be",
                "message":"Est. latitude (dd*mm.mm' N/S):",
                "default":str(positionConfig["Be"]),
                "filter":lambda value:angle.ToJSONCompatible(angle.ToLatitude(angle.ToDecimal(value)))
            },            
            {
                "type":"input",
                "name":"Le",
                "message":"Est. longtitude (dd*mm.mm' E/W):",
                "default":str(positionConfig["Le"]),
                "filter":lambda value:angle.ToJSONCompatible(angle.ToLongtitude(angle.ToDecimal(value)))
            }
        ]
    answers=prompt(questions)

    print("")
    ConfigureObservation("Observation1.cfg", Be=positionConfig["Be"], Le=positionConfig["Le"])
    print("")
    ConfigureObservation("Observation2.cfg", Be=positionConfig["Be"], Le=positionConfig["Le"])
    print("")
    ConfigureObservation("Observation3.cfg", Be=positionConfig["Be"], Le=positionConfig["Le"])
    
    print("\nCalculating fix...\n")
    import threeobjectsfix
    

selectOperationQuestion=[
        {
            "type":"list",
            "name":"Operation",
            "message":"Select operation:",
            "choices":[
                    "Calculate intercept",
                    "Calculate fix from 2 measurements",
                    "Calculate fix from 2 objects",
                    "Calculate fix from 3 objects",
                    "Quit"
                ]
        }
    ]
selectOperationAnswer = prompt(selectOperationQuestion)

if selectOperationAnswer["Operation"]=="Calculate intercept":
    Intercept()
elif selectOperationAnswer["Operation"]=="Calculate fix from 2 measurements":
    OneObjectFix()
elif selectOperationAnswer["Operation"]=="Calculate fix from 2 objects":
    TwoObjectsFix()
elif selectOperationAnswer["Operation"]=="Calculate fix from 3 objects":
    ThreeObjectsFix()
    
print("\nFinished.")
