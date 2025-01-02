import sys
sys.path.append("..\src")

from math import sin, cos, acos, tan, atan, degrees, radians
from astrometry import FindToCoEE
from fix import TwoObjectFix
from timeprocessor import TimeZone, LTtoGMT

phigc0=13.0
lambda0=100.0

v=850/1.852/60
dt=50/60
D=v*dt
hdg=350

phigce=round(phigc0+(D*cos(radians(hdg))),0)
lambdae=round(lambda0+(D*sin(radians(hdg))),0)

print("DR",phigce,lambdae)

aoe=(5*3)+1.5
T=29

Y1=2024
M1=12
D1=21
h1=15
m1=26
s1=00
Y1,M1,D1,h1,m1,s1=LTtoGMT(Y1,M1,D1,h1,m1,s1,lambdae)

a1=153
b1=144
c1=154
Hs1=90.0-degrees(acos((pow(b1,2)+pow(c1,2)-pow(a1,2))/(2*a1*c1)))
#print(Hs1)
Hs1=28.484472 #from Horizon

Y2=2024
M2=12
D2=21
h2=16
m2=5
s2=00
Y2,M2,D2,h2,m2,s2=LTtoGMT(Y2,M2,D2,h2,m2,s2,lambdae)

a2=165
b2=136
c2=154
Hs2=90.0-degrees(acos((pow(b2,2)+pow(c2,2)-pow(a2,2))/(2*a2*c2)))
#print(Hs2)
Hs2=21.270918 #from Horizon

p1,z1=FindToCoEE(phigce,lambdae,Y1,M1,D1,h1,m1,s1,"Sun",Hs1,aoe,T)
p2,z2=FindToCoEE(phigce,lambdae,Y2,M2,D2,h2,m2,s2,"Sun",Hs2,aoe,T)
phigc,lambda_=TwoObjectFix(phigce,lambdae,p1,z1,p2,z2)
print(phigc,lambda_)
'''
iterN=0
while True:
    p1,z1=FindToCoEE(phigce,lambdae,Y1,M1,D1,h1,m1,s1,"Sun",Hs1,aoe,T)
    p2,z2=FindToCoEE(phigce,lambdae,Y2,M2,D2,h2,m2,s2,"Sun",Hs2,aoe,T)
    phigc,lambda_=TwoObjectFix(phigce,lambdae,p1,z1,p2,z2)
    if (abs(phigce-phigc)<1e-6 and abs(lambdae-lambda_)<1e-6) or iterN>50:
        break
    else:
        phigce=phigc
        lambdae=lambda_
        iterN=iterN+1
print(phigc,lambda_)
'''
