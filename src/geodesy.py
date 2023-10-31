#Geodesic algorithms
#Based on description in Wiki: https://en.wikipedia.org/wiki/Great-circle_navigation
#Additional info: https://en.wikipedia.org/wiki/Geodesics_on_an_ellipsoid
import angle
from trigonometry import sin, cos, tg, arcsin, arctg, atan2
from math import sqrt, pow, radians, degrees, pi

f=1/298.257223563 #Earth flattening factor, from article at https://www.vcalc.com/wiki/vcalc/geocentric-to-geodetic-latitude

def GeocentricToGeodetic(Bgc):
    return arctg((1/pow(1-f,2))*tg(Bgc)) #formula from https://www.vcalc.com/wiki/vcalc/geocentric-to-geodetic-latitude

def GeodeticToGeocentric(Bgd):
    return arctg(pow(1-f,2)*tg(Bgd)) #formula from https://www.vcalc.com/wiki/vcalc/geodetic-to-geocentric-latitude; use this for convert calculated coords (achieved values closer to truth)

class Point:
    def __init__(self, B, L):
        self.B=angle.ToDecimal(B)
        self.L=angle.ToDecimal(L)

class Orthodromy:
    def __init__(self, *args, **kvargs): 
        self.planetRadius=kvargs.get("planetRadius", 3440.0) #planet radius for Earth
        
        self.startPoint=kvargs.get("startPoint", None)
        self.destinationPoint=kvargs.get("destinationPoint",None)
        self.startHDG=kvargs.get("startHDG",None)
        self.length=kvargs.get("length",None)
        
        if (not self.startPoint is None) and (not self.destinationPoint is None) and (self.startHDG is None) and (self.length is None):
            self.startHDG, self.destinationHDG, self.angularLength, self.length = Orthodromy.CalculateFrom2Pts(self.startPoint, self.destinationPoint, self.planetRadius)
        elif (not self.startPoint is None) and (self.destinationPoint is None) and (not self.startHDG is None) and (not self.length is None):
            B, L, self.destinationHDG, self.angularLength = Orthodromy.CalculateFromPtHdgDist(self.startPoint, self.startHDG, self.length, self.planetRadius)
            self.destinationPoint = Point(B,L)
            

    def CalculateFrom2Pts(p1, p2, R): #point1 (start), point2 (destination), and planet radius
        dL=p2.L-p1.L

        alpha1 = atan2( cos(p2.B)*sin(dL), (cos(p1.B)*sin(p2.B))-(sin(p1.B)*cos(p2.B)*cos(dL)) )    #heading at start
        alpha2 = atan2( cos(p1.B)*sin(dL), (-cos(p2.B)*sin(p1.B))+(sin(p2.B)*cos(p1.B)*cos(dL)) )   #heading at destination

        delta12=atan2( sqrt( pow((cos(p1.B)*sin(p2.B))-(sin(p1.B)*cos(p2.B)*cos(dL)), 2) + pow(cos(p2.B)*sin(dL), 2) ), (sin(p1.B)*sin(p2.B))+(cos(p1.B)*cos(p2.B)*cos(dL)) ) #angular length of arc of great circle

        s12=R*radians(delta12) #real length of arc - great-circle or orthodromic distance

        return [alpha1, alpha2, delta12, s12]

    def CalculateFromPtHdgDist(p1, alpha1, s12, R): #point1 (start), HDG at start, distance and planet radius
        delta12=degrees(s12/R)

        B,L,alpha2=Orthodromy.FindWaypointFor(p1, alpha1, delta12, s12, s12)
        
        return [B, L, alpha2, delta12]

    def FindWaypointFor(p1, alpha1, delta12, s12, d):
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

    def FindWaypointAt(self, distance):
        return Orthodromy.FindWaypointFor(self.startPoint, self.startHDG, self.angularLength, self.length, distance)
