import sys
sys.path.append("..\src")

import almanac
from math import sin, cos, acos, tan, atan, degrees, radians, sqrt
from astrometry import ElevationCorrection, FindToCoEE
from position import FromToCoEEo3CO
import orthodromy

from external.astro import *

print("Palomar observatory (spring 2024) practical test.")
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
M1=4
D1=12
h1=16
m1=0
s1=0
Hs1=32.394512
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=4
D2=12
h2=17
m2=0
s2=0
Hs2=44.387954
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=4
D3=12
h3=18
m3=0
s3=0
Hs3=55.241435
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
M1=4
D1=12
h1=1
m1=0
s1=0
Hs1=58.678283
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1,limb=0)

Y2=2024
M2=4
D2=12
h2=2
m2=0
s2=0
Hs2=46.540710
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2,limb=0)

Y3=2024
M3=4
D3=12
h3=3
m3=0
s3=0
Hs3=34.511650
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
M1=4
D1=12
h1=16
m1=0
s1=0
Hs1=38.061296
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=4
D2=12
h2=17
m2=0
s2=0
Hs2=48.417239
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=4
D3=12
h3=18
m3=0
s3=0
Hs3=56.113461
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
M1=4
D1=12
h1=16
m1=0
s1=0
Hs1=44.360838
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=4
D2=12
h2=17
m2=0
s2=0
Hs2=49.279338
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=4
D3=12
h3=18
m3=0
s3=0
Hs3=49.519159
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
M1=4
D1=12
h1=18
m1=0
s1=0
Hs1=39.779015
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=4
D2=12
h2=19
m2=0
s2=0
Hs2=52.103900
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=4
D3=12
h3=20
m3=0
s3=0
Hs3=63.567270
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
M1=4
D1=12
h1=18
m1=0
s1=0
Hs1=48.471010
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=4
D2=12
h2=19
m2=0
s2=0
Hs2=43.735579
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=4
D3=12
h3=20
m3=0
s3=0
Hs3=35.580685
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
M1=4
D1=12
h1=1
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=62.5393 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2024
M2=4
D2=12
h2=2
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=55.3882
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2024
M3=4
D3=12
h3=3
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=45.0103
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
M1=4
D1=12
h1=1
m1=0
s1=0
#Hs1=ElevationFor(celestialObjectName,phi0,lambda0,Y1,M1,D1,h1,m1,s1)
Hs1=62.6591 #from NAOJ (https://eco.mtk.nao.ac.jp/cgi-bin/koyomi/cande/horizontal_rhip_en.cgi)
Hs1+=ElevationCorrection(celestialObjectName,Y1,M1,D1,h1,m1,s1,Hs1)

Y2=2010
M2=4
D2=12
h2=2
m2=0
s2=0
#Hs2=ElevationFor(celestialObjectName,phi0,lambda0,Y2,M2,D2,h2,m2,s2)
Hs2=55.6360
Hs2+=ElevationCorrection(celestialObjectName,Y2,M2,D2,h2,m2,s2,Hs2)

Y3=2010
M3=4
D3=12
h3=3
m3=0
s3=0
#Hs3=ElevationFor(celestialObjectName,phi0,lambda0,Y3,M3,D3,h3,m3,s3)
Hs3=45.3162
Hs3+=ElevationCorrection(celestialObjectName,Y3,M3,D3,h3,m3,s3,Hs3)

deltael1,beta1=FindToCoEE(phiAP,lambdaAP,Y1,M1,D1,h1,m1,s1,celestialObjectName,Hs1)
deltael2,beta2=FindToCoEE(phiAP,lambdaAP,Y2,M2,D2,h2,m2,s2,celestialObjectName,Hs2)
deltael3,beta3=FindToCoEE(phiAP,lambdaAP,Y3,M3,D3,h3,m3,s3,celestialObjectName,Hs3)
phigc,lambda_=FromToCoEEo3CO(phiAP,lambdaAP,deltael1,beta1,deltael2,beta2,deltael3,beta3)
alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phigc,lambda_,phi0,lambda0)
print(celestialObjectName,round(phigc,9),round(lambda_,9),round(alpha1,1),round(s12,3))
