import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians
from astrometry import CalculateIntercept
from fix import TwoObjectFix, ThreeObjectFix
from timeprocessor import TimeZone, LTtoGMT
import angle

almanac.source=1

phigce=round(33.3562)
lambdae=round(-116.865)

print("DR LAT:",phigce,"DR LON:",lambdae)

Y1=2024
M1=12
D1=25
h1=6
m1=0
s1=0
Hs1=36.976441

Y2=2024
M2=12
D2=25
h2=7
m2=0
s2=0
Hs2=49.530780

Y3=2024
M3=12
D3=25
h3=8
m3=0
s3=0
Hs3=61.948086

p1,z1=CalculateIntercept(phigce,lambdae,Y1,M1,D1,h1,m1,s1,"Mars",Hs1)
print(p1,z1)
p2,z2=CalculateIntercept(phigce,lambdae,Y2,M2,D2,h2,m2,s2,"Mars",Hs2)
print(p2,z2)
p3,z3=CalculateIntercept(phigce,lambdae,Y3,M3,D3,h3,m3,s3,"Mars",Hs3)
print(p3,z3)
phigc,lambda_=TwoObjectFix(phigce,lambdae,p1,z1,p2,z2)
print("2 obj fix: ",phigc,lambda_)
phigc,lambda_=ThreeObjectFix(phigce,lambdae,p1,z1,p2,z2,p3,z3)
print("3 obj fix: ",phigc,lambda_)
