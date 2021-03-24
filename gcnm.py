#Great circle navigation machine
#Based on description in Wiki: https://en.wikipedia.org/wiki/Great-circle_navigation
import json
import angle
from trigonometry import sin, cos, tg, arcsin, arctg, atan2
from math import sqrt, pow, radians, degrees, pi
import timeprocessor

class Point:
    def __init__(self, B, L):
        self.B=angle.ToDecimal(B)
        self.L=angle.ToDecimal(L)

class Orthodromy:
    def __init__(self, startPoint, destinationPoint, planetRadius=3440.0): #default planet radius configured for Earth
        self.startPoint=startPoint
        self.destinationPoint=destinationPoint
        self.planetRadius = planetRadius
        self.Calculate()

    def Calculate(self):
        p1=self.startPoint
        p2=self.destinationPoint
        R=self.planetRadius

        dL=p2.L-p1.L

        alpha1 = atan2( cos(p2.B)*sin(dL), (cos(p1.B)*sin(p2.B))-(sin(p1.B)*cos(p2.B)*cos(dL)) )    #heading at start
        alpha2 = atan2( cos(p1.B)*sin(dL), (-cos(p2.B)*sin(p1.B))+(sin(p2.B)*cos(p1.B)*cos(dL)) )   #heading at destination

        delta12=atan2( sqrt( pow((cos(p1.B)*sin(p2.B))-(sin(p1.B)*cos(p2.B)*cos(dL)), 2) + pow(cos(p2.B)*sin(dL), 2) ), (sin(p1.B)*sin(p2.B))+(cos(p1.B)*cos(p2.B)*cos(dL)) ) #angular length of arc of great circle

        s12=R*radians(delta12) #real length of arc - great-circle or orthodromic distance

        self.startHDG=alpha1
        self.destinationHDG=alpha2
        self.angularLength=delta12
        self.Length=s12

    def FindWaypointAt(self, distance):
        p1=self.startPoint
        alpha1=self.startHDG
        delta12=self.angularLength
        s12=self.Length
        d=distance

        alpha0 = atan2( sin(alpha1)*cos(p1.B), sqrt( pow(cos(alpha1),2) + (pow(sin(alpha1),2)*pow(sin(p1.B),2)) ) )

        if p1.B==0 and alpha1==degrees(pi/2):
            delta01=0
        else:
            delta01=atan2(tg(p1.B), cos(alpha1))

        delta02 = delta01+delta12

        L01=atan2( sin(alpha0)*sin(delta01), cos(delta01) )
        L0=p1.L-L01

        if d>s12:
            print("Error: travelled distance greater than caclulated orthodromic distance.")
            return None

        delta=delta01+(delta12*(d/s12)) #delta = delta01+(d/R) not working in our case, because we using angles in degrees, not in radians

        B = atan2( cos(alpha0)*sin(delta), sqrt( pow(cos(delta),2) + (pow(sin(alpha0),2)*pow(sin(delta),2)) ) )
        L = atan2( sin(alpha0)*sin(delta), cos(delta) ) + L0
        alpha = atan2( tg(alpha0), cos(delta) ) #heading at dead reconking

        return [B, L, alpha]        

configFile=open("Route.cfg")
config = json.loads(configFile.read())

p1=Point(config["Start"]["Latitude"], config["Start"]["Longtitude"])
p2=Point(config["Destination"]["Latitude"], config["Destination"]["Longtitude"])
d = float(config["Distance travelled, nmi"])

orthodromy = Orthodromy(p1,p2)
B,L,alpha = orthodromy.FindWaypointAt(d)

print("DR:")
print(angle.ToLatitude(B))
print(angle.ToLongtitude(L))

magC = float(config["Magnetic compass correction"])
magHDG = alpha+magC #heading after magnetic correction

v=float(config["Current speed, kts"])
V=[v*cos(magHDG), v*sin(magHDG)] #velocity vector

wDir=float(angle.ToDecimal(config["Wind"]["Direction"]))
wV=float(config["Wind"]["Speed, kts"])
W=[wV*cos(wDir), wV*sin(wDir)] #wind vector

M=[V[0]+W[0], V[1]+W[1]] #movement vector

windC=magHDG-atan2(M[1], M[0]) #wind drift correction
HDG=magHDG+windC #heading after magnetic correction and wind drift correction

print("")
print("HDG: " + angle.ToString(round(HDG,0)))

dtd = orthodromy.Length-d
print("DTD, nmi: " + str(round(dtd,0)))

eta = timeprocessor.ToString(round(timeprocessor.HoursToSeconds(dtd/v),0))
print("ETA: " + eta)


