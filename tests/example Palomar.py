import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians
from astrometry import CalculateIntercept
from fix import TwoObjectFix, ThreeObjectFix
from timeprocessor import TimeZone, LTtoGMT

almanac.source=1

phigce=33
lambdae=-116

aoe=1712.0
T=15

print("DR LAT:",phigce,"DR LON:",lambdae)

timeZone=TimeZone(lambdae)
print("Time zone, UTC:",timeZone)

Y1=2024
M1=12
D1=25
h1=6
m1=0
s1=0

Hs1=33.045921

Y2=2024
M2=12
D2=25
h2=7
m2=0
s2=0

Hs2=44.978511

Y3=2024
M3=12
D3=25
h3=8
m3=0
s3=0

Hs3=56.733313

p1,z1=CalculateIntercept(phigce,lambdae,Y1,M1,D1,h1,m1,s1,"Mars",Hs1,aoe,T)
p2,z2=CalculateIntercept(phigce,lambdae,Y2,M2,D2,h2,m2,s2,"Mars",Hs2,aoe,T)
p3,z3=CalculateIntercept(phigce,lambdae,Y3,M3,D3,h3,m3,s3,"Mars",Hs3,aoe,T)
phigc,lambda_=TwoObjectFix(phigce,lambdae,p1,z1,p2,z2)
print("2 obj fix LAT:",phigc,"LON:",lambda_)
phigc,lambda_=ThreeObjectFix(phigce,lambdae,p1,z1,p2,z2,p3,z3)
print("3 obj fix LAT:",phigc,"LON:",lambda_)
        
