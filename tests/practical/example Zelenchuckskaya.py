import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians
from astrometry import FindToCoEE
from fix import TwoObjectFix, ThreeObjectFix
import angle

almanac.source=1

phigce=round(43.787377)
lambdae=round(41.564968)

print("DR",phigce,lambdae)

Y1=2024
M1=12
D1=25
h1=11
m1=00
s1=00
Hs1=26.548675

Y2=2024
M2=12
D2=25
h2=12
m2=00
s2=00
Hs2=29.646250

Y3=2024
M3=12
D3=25
h3=13
m3=00
s3=00
Hs3=29.704617

p1,z1=FindToCoEE(phigce,lambdae,Y1,M1,D1,h1,m1,s1,"Venus",Hs1)
p2,z2=FindToCoEE(phigce,lambdae,Y2,M2,D2,h2,m2,s2,"Venus",Hs2)
p3,z3=FindToCoEE(phigce,lambdae,Y3,M3,D3,h3,m3,s3,"Venus",Hs3)
phigc,lambda_=TwoObjectFix(phigce,lambdae,p1,z1,p2,z2)
print("2 obj fix: ",phigc,lambda_)
phigc,lambda_=ThreeObjectFix(phigce,lambdae,p1,z1,p2,z2,p3,z3)
print("3 obj fix: ",phigc,lambda_)
        
