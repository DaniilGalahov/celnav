from external.math import *

import equationsolver as solve

def FromToCoEEo2CO(phiAP,lambdaAP,p1,gamma1,p2,gamma2):
    y,x=solve.LinEq22(cos(radians(gamma1)),sin(radians(gamma1)),p1,cos(radians(gamma2)),sin(radians(gamma2)),p2)
    phigc=phiAP+y
    lambda_=lambdaAP-(x/cos(radians(phigc)))    
    return phigc,lambda_

def FromToCoEEo3CO(phiAP,lambdaAP,p1,gamma1,p2,gamma2,p3,gamma3):
    phigc1,lambda1=FromToCoEEo2CO(phiAP,lambdaAP,p1,gamma1,p2,gamma2)
    phigc2,lambda2=FromToCoEEo2CO(phiAP,lambdaAP,p2,gamma2,p3,gamma3)
    phigc3,lambda3=FromToCoEEo2CO(phiAP,lambdaAP,p3,gamma3,p1,gamma1)
    phigc=(phigc1+phigc2+phigc3)/3.0
    lambda_=(lambda1+lambda2+lambda3)/3.0
    return phigc,lambda_
