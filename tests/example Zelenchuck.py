import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians
from astrometry import CalculateIntercept
from fix import TwoObjectFix, ThreeObjectFix
from timeprocessor import TimeZone, LTtoGMT
import angle

almanac.source=1

phigce=round(angle.ToDecimal(43.787377))
lambdae=round(angle.ToDecimal(41.564968))

aoe=1175.0
T=15

print("DR LAT:",phigce,"DR LON:",lambdae)

timeZone=TimeZone(lambdae)
print("Time zone, UTC:",timeZone)

Y1=2024
M1=12
D1=25
h1=9
m1=55
s1=57.6
Y1,M1,D1,h1,m1,s1=LTtoGMT(Y1,M1,D1,h1,m1,s1,lambdae)

Hs1=20.341908

Y2=2024
M2=12
D2=25
h2=11
m2=55
s2=46.08
Y2,M2,D2,h2,m2,s2=LTtoGMT(Y2,M2,D2,h2,m2,s2,lambdae)

Hs2=29.302336

Y3=2024
M3=12
D3=25
h3=13
m3=10
s3=38.880
Y3,M3,D3,h3,m3,s3=LTtoGMT(Y3,M3,D3,h3,m3,s3,lambdae)

Hs3=29.047881

p1,z1=CalculateIntercept(phigce,lambdae,Y1,M1,D1,h1,m1,s1,"Venus",Hs1,aoe,T)
p2,z2=CalculateIntercept(phigce,lambdae,Y2,M2,D2,h2,m2,s2,"Venus",Hs2,aoe,T)
p3,z3=CalculateIntercept(phigce,lambdae,Y3,M3,D3,h3,m3,s3,"Venus",Hs3,aoe,T)
phigc,lambda_=TwoObjectFix(phigce,lambdae,p1,z1,p2,z2)
print("2 obj fix LAT:",phigc,"LON:",lambda_)
phigc,lambda_=ThreeObjectFix(phigce,lambdae,p1,z1,p2,z2,p3,z3)
print("3 obj fix LAT:",phigc,"LON:",lambda_)
        
