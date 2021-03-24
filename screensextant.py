#calculate angular coordinates of object in MSFS2004 by its image on monitor
import json
import math
import angle
from trigonometry import sin, cos, tg, arcsin, arctg

configFile=open("Screen sextant.cfg")
config = json.loads(configFile.read())
configFile.close()

focalLengthAtZoom05=float(config["Focal length"]["0.5"]) #mm
focalLengthAtZoom10=float(config["Focal length"]["1.0"]) #mm

monitorWidth=float(config["Monitor size"]["Width"]) #mm
monitorHeight=float(config["Monitor size"]["Height"]) #mm

monitorCenterX=monitorWidth/2
monitorCenterY=monitorHeight/2

monitorWidthInPixels=int(config["Monitor resolution"]["Width"])
monitorHeightInPixels=int(config["Monitor resolution"]["Height"])

x=float(config["x"]) #Coordinates measuring from bottom left corner
y=float(config["y"])
usePixels=config["Measured in pixels"]

viewDirection=float(config["Direction of view"]) #CC from HDG
zoomLevel=float(config["Zoom level"])

if(usePixels):
    x=(x/monitorWidthInPixels)*monitorWidth
    y=monitorHeight-((y/monitorHeightInPixels)*monitorHeight) #in Paint coordinates measuring from top ledt corner, so we converting them

xOffset = x-monitorCenterX
yOffset = y-monitorCenterY

focalLength=focalLengthAtZoom05    
if(zoomLevel==1.0):
    focalLength=focalLengthAtZoom05

Z=viewDirection+arctg(xOffset/focalLength)
H=arctg(yOffset/focalLength)

print("Azimuth from HDG: "+angle.ToString(Z))
print("Height: "+angle.ToString(H))
