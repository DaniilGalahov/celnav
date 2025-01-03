from external.math import *

import equationsolver as solve

def FixLoPIntersection(phigce,lambdae,p1,z1,p2,z2): #obsolette, left for compatibility
    x,y=solve.LinEq22(sin(radians(z1)),cos(radians(z1)),p1,sin(radians(z2)),cos(radians(z2)),p2)
    phigc=phigce+(y/60.0)    
    lambda_=lambdae+(x/60.0/cos(radians(phigc)))
    return phigc,lambda_

def LambdaCorrection(x):
    y=(-0.00000000338486755329*pow(x,3))+(-0.00000006557786127051*pow(x,2))+(0.00009836819808222858*pow(x,1))+(0.00085718742396453271)
    return y 

def FixToCoEEIntersection(phiAP,lambdaAP,p1,gamma1,p2,gamma2):
    y,x=solve.LinEq22(cos(radians(gamma1)),sin(radians(gamma1)),p1,cos(radians(gamma2)),sin(radians(gamma2)),p2)
    phigc=phiAP+y
    lambda_=lambdaAP-(x/cos(radians(phigc)))
    lambda_-=LambdaCorrection(lambda_)
    return phigc,lambda_

def TwoObjectFix(phiAP,lambdaAP,p1,gamma1,p2,gamma2):
    return FixToCoEEIntersection(phiAP,lambdaAP,p1,gamma1,p2,gamma2)

def ThreeObjectFix(phiAP,lambdaAP,p1,gamma1,p2,gamma2,p3,gamma3):
    phigc1,lambda1=FixToCoEEIntersection(phiAP,lambdaAP,p1,gamma1,p2,gamma2)
    phigc2,lambda2=FixToCoEEIntersection(phiAP,lambdaAP,p2,gamma2,p3,gamma3)
    phigc3,lambda3=FixToCoEEIntersection(phiAP,lambdaAP,p3,gamma3,p1,gamma1)
    phigc=(phigc1+phigc2+phigc3)/3.0
    lambda_=(lambda1+lambda2+lambda3)/3.0
    return phigc,lambda_
