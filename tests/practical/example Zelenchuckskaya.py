import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians, sqrt
from astrometry import ElevationCorrection, FindToCoEE, ElevationFor
from fix import TwoObjectFix, ThreeObjectFix

from external.astro import *

almanac.source=1

phi0=43.64675 #Zelenchukskaya observatory - BTA6 (precisely)
lambda0=41.4400953

phiAP=round(phi0)
lambdaAP=round(lambda0)

print("DR",phiAP,lambdaAP)

#---------- Sun ----------
celestialObjectName="Sun"

Y1=2024
M1=12
D1=25
h1=7
m1=0
s1=0
Hs1=16.274200
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=12
D2=25
h2=8
m2=0
s2=0
Hs2=20.872734
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=12
D3=25
h3=9
m3=0
s3=0
Hs3=22.932175
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))


#---------- Moon ----------
celestialObjectName="Moon"

Y1=2024
M1=12
D1=25
h1=2
m1=0
s1=0
Hs1=22.992909
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=12
D2=25
h2=3
m2=0
s2=0
Hs2=28.832887
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=12
D3=25
h3=4
m3=0
s3=0
Hs3=32.131676
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))


#---------- Venus ----------
celestialObjectName="Venus"

Y1=2024
M1=12
D1=25
h1=13
m1=0
s1=0
Hs1=29.704698
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=14
m2=0
s2=0
Hs2=26.715479
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=15
m3=0
s3=0
Hs3=21.094889
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))


#---------- Mars ----------
celestialObjectName="Mars"

Y1=2024
M1=12
D1=25
h1=1
m1=0
s1=0
Hs1=61.670786
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=2
m2=0
s2=0
Hs2=52.258818
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=3
m3=0
s3=0
Hs3=41.719817
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))


#---------- Jupiter ----------
celestialObjectName="Jupiter"

Y1=2024
M1=12
D1=25
h1=17
m1=0
s1=0
Hs1=49.466174
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=18
m2=0
s2=0
Hs2=59.120867
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=19
m3=0
s3=0
Hs3=66.246954
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))


#---------- Saturn ----------
celestialObjectName="Saturn"

Y1=2024
M1=12
D1=25
h1=12
m1=0
s1=0
Hs1=31.496362
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=-1)

Y2=2024
M2=12
D2=25
h2=13
m2=0
s2=0
Hs2=36.480069
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=-1)

Y3=2024
M3=12
D3=25
h3=14
m3=0
s3=0
Hs3=38.267456
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=-1)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))


#---------- Betelgeuse ----------
celestialObjectName="Betelgeuse"

Y1=2024
M1=12
D1=25
h1=21
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=53.7277 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=22
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=50.7720
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=23
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=44.1175
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))

#JD24=JulianDate(Y3,M3,D3,h3,m3,s3)


#---------- Betelgeuse 2010 ----------
celestialObjectName="Betelgeuse"

Y1=2010
M1=12
D1=25
h1=21
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=53.7411 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2010
M2=12
D2=25
h2=22
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=50.9051
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2010
M3=12
D3=25
h3=23
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=44.3327
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=ThreeObjectFix(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
d=(sqrt(pow(phigc-phi0,2)+pow(lambda_-lambda0,2)))*60*1.852*cos(radians(phigc))
print(celestialObjectName,phigc,lambda_,round(d,3))
