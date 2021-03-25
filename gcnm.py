#Great circle navigation machine
#Based on description in Wiki: https://en.wikipedia.org/wiki/Great-circle_navigation
import json
import angle
from geodesy import Point, Orthodromy
from trigonometry import sin, cos, tg, arcsin, arctg, atan2
from math import sqrt, pow, radians, degrees, pi
from numpy import array as vector, linalg as vectorOperations
import timeprocessor

configFile=open("Route.cfg")
config = json.loads(configFile.read())
configFile.close()

p1=Point(config["Start"]["Latitude"], config["Start"]["Longtitude"])
p2=Point(config["Destination"]["Latitude"], config["Destination"]["Longtitude"])
D=float(config["Distance travelled, nmi"])
d=float(config["Distance to next waypoint, nmi"])

orthodromy = Orthodromy(startPoint=p1,destinationPoint=p2)
B,L,alpha = orthodromy.FindWaypointAt(D) #calculated position and true heading

magC = float(config["Magnetic compass correction"])
magHDG = alpha+magC #heading after magnetic correction

v=float(config["Desired speed, kts"])
V=vector([v*cos(magHDG), v*sin(magHDG)]) #velocity vector

wDir=float(angle.ToDecimal(config["Wind"]["Direction"]))
wV=float(config["Wind"]["Speed, kts"])
W=vector([wV*cos(wDir), wV*sin(wDir)]) #wind vector

M=V+W #movement vector

windC=magHDG-atan2(M[1], M[0]) #wind drift correction
HDG=magHDG+windC #heading after magnetic correction and wind drift correction

dtd = orthodromy.length-D #distance to destination

t=d/vectorOperations.norm(M) #time to next waypoint
if dtd<d:
    t=dtd/vectorOperations.norm(M)

print("")
print("Current state:")
print("DR: "+angle.ToLatitude(B)+" / "+angle.ToLongtitude(L))
print("TD, nmi: "+str(round(D,0))) 
print("DtD, nmi: " + str(round(dtd,0)))

print("")
print("Navigation solution:")
print("Wpt HDG: " + str(round(HDG,0))+"°")
print("Wpt ETA: " + timeprocessor.ToString(round(timeprocessor.HoursToSeconds(t),0)))
