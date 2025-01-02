import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians
from astrometry import FindToCoEE
from fix import TwoObjectFix, ThreeObjectFix
import angle

almanac.source=1

phiAP=round(33.3562)
lambdaAP=round(-116.865)

print("DR",phiAP,lambdaAP)

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

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,"Mars",Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,"Mars",Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,"Mars",Hs3)
phigc,lambda_=TwoObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2)
print("2 obj fix: ",phigc,lambda_)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
print("3 obj fix: ",phigc,lambda_)
