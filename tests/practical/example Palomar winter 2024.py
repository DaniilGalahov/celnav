import setup

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians, sqrt
from astrometry import ElevationCorrection, FindToCoEE
from position import FromToCoEEo3CO
import orthodromy

from external.astro import *

print("Palomar observatory (winter 2024) practical test.")
almanac.source=1

phi0=33.3562811 #Palomar observatory (precisely)
lambda0=-116.8651156
print("OP:",phi0,lambda0)

phiAP=round(phi0)
lambdaAP=round(lambda0)

print("DR:",phiAP,lambdaAP)

#---------- Sun ----------
celestialObjectName="Sun"

Y1=2024
M1=12
D1=25
h1=18
m1=0
s1=0
Hs1=27.766345
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=12
D2=25
h2=19
m2=0
s2=0
Hs2=32.172951
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=12
D3=25
h3=20
m3=0
s3=0
Hs3=33.235187
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Moon ----------
celestialObjectName="Moon"

Y1=2024
M1=12
D1=25
h1=13
m1=0
s1=0
Hs1=29.814215
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=12
D2=25
h2=14
m2=0
s2=0
Hs2=36.631357
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=12
D3=25
h3=15
m3=0
s3=0
Hs3=40.330848
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3,limb=0)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Venus ----------
celestialObjectName="Venus"

Y1=2024
M1=12
D1=25
h1=21
m1=0
s1=0
Hs1=32.322042
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=22
m2=0
s2=0
Hs2=38.200181
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=23
m3=0
s3=0
Hs3=40.518367
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Mars ----------
celestialObjectName="Mars"

Y1=2024
M1=12
D1=25
h1=6
m1=0
s1=0
Hs1=36.976441
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=7
m2=0
s2=0
Hs2=49.530780
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=8
m3=0
s3=0
Hs3=61.948086
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Jupiter ----------
celestialObjectName="Jupiter"

Y1=2024
M1=12
D1=25
h1=6
m1=0
s1=0
Hs1=77.584226
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=7
m2=0
s2=0
Hs2=75.654424
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=8
m3=0
s3=0
Hs3=65.321337
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Saturn ----------
celestialObjectName="Saturn"

Y1=2024
M1=12
D1=25
h1=1
m1=0
s1=0
Hs1=48.133563
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=2
m2=0
s2=0
Hs2=43.927505
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=3
m3=0
s3=0
Hs3=36.158993
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Betelgeuse ----------
celestialObjectName="Betelgeuse"

Y1=2024
M1=12
D1=25
h1=3
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=23.3776 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=12
D2=25
h2=4
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=35.6652
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=12
D3=25
h3=5
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=47.2546
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))


#---------- Betelgeuse 2010 ----------
celestialObjectName="Betelgeuse"

Y1=2010
M1=12
D1=25
h1=3
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=23.0349 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2010
M2=12
D2=25
h2=4
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=35.3335
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2010
M3=12
D3=25
h3=5
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=46.9511
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))
