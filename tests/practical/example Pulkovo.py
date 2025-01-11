import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians, sqrt
from astrometry import ElevationCorrection, FindToCoEE
from fix import TwoObjectFix, ThreeObjectFix

from external.astro import *

print("Pulkovo observatory practical test.")
almanac.source=1

phi0=59.7719364 #Pulkovo observatory - Main cupola (precisely)
lambda0=30.3260356
print("OP:",phi0,lambda0)

phiAP=round(phi0)
lambdaAP=round(lambda0)

print("DR:",phiAP,lambdaAP)

#---------- Sun ----------
celestialObjectName="Sun"

Y1=2024
M1=12
D1=25
h1=9
m1=0
s1=0
Hs1=6.114364
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=12
D2=25
h2=10
m2=0
s2=0
Hs2=6.975771
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=12
D3=25
h3=11
m3=0
s3=0
Hs3=6.053619
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Moon ----------
celestialObjectName="Moon"

Y1=2024
M1=12
D1=25
h1=3
m1=0
s1=0
Hs1=11.476569
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=12
D2=25
h2=4
m2=0
s2=0
Hs2=14.715417
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=12
D3=25
h3=5
m3=0
s3=0
Hs3=16.225734
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Venus ----------
celestialObjectName="Venus"

Y1=2024
M1=12
D1=25
h1=12
m1=0
s1=0
Hs1=12.459602
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=13
m2=0
s2=0
Hs2=13.924194
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=14
m3=0
s3=0
Hs3=13.465523
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Mars ----------
celestialObjectName="Mars"

Y1=2024
M1=12
D1=25
h1=1
m1=0
s1=0
Hs1=52.060180
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=2
m2=0
s2=0
Hs2=48.393650
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=3
m3=0
s3=0
Hs3=42.727399
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Jupiter ----------
celestialObjectName="Jupiter"

Y1=2024
M1=12
D1=25
h1=16
m1=0
s1=0
Hs1=29.974634
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=17
m2=0
s2=0
Hs2=37.271650
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=18
m3=0
s3=0
Hs3=43.802138
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Saturn ----------
celestialObjectName="Saturn"

Y1=2024
M1=12
D1=25
h1=13
m1=0
s1=0
Hs1=19.026251
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=14
m2=0
s2=0
Hs2=21.577610
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=15
m3=0
s3=0
Hs3=22.093696
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Betelgeuse ----------
celestialObjectName="Betelgeuse"

Y1=2024
M1=12
D1=25
h1=21
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=37.2234 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=22
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=37.4579
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=23
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=35.2717
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(d,3))


#---------- Betelgeuse 2010 ----------
celestialObjectName="Betelgeuse"

Y1=2010
M1=12
D1=25
h1=21
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=37.1788 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2010
M2=12
D2=25
h2=22
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=37.4807
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2010
M3=12
D3=25
h3=23
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=35.3579
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,"y.2010",round(phigc,9),round(lambda_,9),round(d,3))
