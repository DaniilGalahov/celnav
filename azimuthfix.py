#determine current position by capturing two azimuths
import json
import angle
import math
from trigonometry import sin, cos, tg, arcsin, arctg
import equationsolver as es

configFile=open("Azimut fix.cfg")
config = json.loads(configFile.read())

bearing1=angle.ToDecimal(config["Object1"]["Bearing"]) #azimuth from N to object 1
x1=-angle.ToDecimal(config["Object1"]["Longtitude"]) #Longtitude of object 1
y1=-angle.ToDecimal(config["Object1"]["Latitude"]) #Latitude of object 1

bearing2=angle.ToDecimal(config["Object2"]["Bearing"]) #azimuth from N to object 2
x2=-angle.ToDecimal(config["Object2"]["Longtitude"]) #Longtitude of object 2
y2=-angle.ToDecimal(config["Object2"]["Latitude"]) #Latitude of object 2


def AlphaFrom(bearing):
    return 90.0-bearing

def TethaFrom(alpha):
    return alpha+math.degrees(math.pi/2.0)

def pFrom(alpha, x, y):
    p=y
    
    alpha=alpha%360
    if alpha!=0.0 and alpha!=180.0:
        b=y-(tg(alpha)*x)
        x0=-b/tg(alpha)
        p=x0*sin(alpha)

    return p

alpha1=AlphaFrom(bearing1)
alpha2=AlphaFrom(bearing2)

tetha1=TethaFrom(alpha1)
tetha2=TethaFrom(alpha2)

p1=pFrom(alpha1,x1,y1)
p2=pFrom(alpha2,x2,y2)

x,y = es.LinEq22(cos(tetha1), sin(tetha1), p1, cos(tetha2), sin(tetha2), p2)

#print(x)
#print(y)

print(str(angle.ToLongtitude(x)))
print(str(angle.ToLatitude(y)))


