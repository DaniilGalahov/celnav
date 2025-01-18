#Position determination algorithms
from external.math import *
from external.astro import *

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

def FromP3A3(phi1,lambda1,phi2,lambda2,phi3,lambda3,alpha12,alpha23,alpha31): #phigc1,lambda1,phigc2,lambda2,phigc3,lambda3, angle between pt 1 and 2, angle between pt 2 and 3, angle between pt 3 and 1; Realization of Tienstra method
    Na=phi1
    Ea=lambda1
    Nb=phi2
    Eb=lambda2
    Nc=phi3
    Ec=lambda3
    a=alpha23
    b=alpha31
    c=alpha12
    vector_AB=vector([Eb,Nb])-vector([Ea,Na])
    vector_BC=vector([Ec,Nc])-vector([Eb,Nb])
    vector_CA=vector([Ea,Na])-vector([Ec,Nc])
    A=angleBetween(vector_AB,-vector_CA)
    B=angleBetween(-vector_AB,vector_BC)
    C=angleBetween(-vector_BC,vector_CA)
    n1=1.0/((1.0/tan(radians(A)))-(1.0/tan(radians(a))))
    n2=1.0/((1.0/tan(radians(B)))-(1.0/tan(radians(b))))
    n3=1.0/((1.0/tan(radians(C)))-(1.0/tan(radians(c))))
    Np=((n1*Na)+(n2*Nb)+(n3*Nc))/(n1+n2+n3)
    Ep=((n1*Ea)+(n2*Eb)+(n3*Ec))/(n1+n2+n3)
    return Np,Ep

def FromP3R3(phi1,lambda1,phi2,lambda2,phi3,lambda3,r1,r2,r3): #phigc1,lambda1,phigc2,lambda2,phigc3,lambda3,range,range2,range3; RANGES MUST BE IN KILOMETERS!; Realization of trilateration method from "Robust Trilateration Based Algorithm for Indoor Positioning Systems"
    def KmToGD(x):
        return x/1.852/60.0
    y1=phi1
    x1=lambda1
    y2=phi2
    x2=lambda2
    y3=phi3
    x3=lambda3
    d1=KmToGD(r1)
    d2=KmToGD(r2)
    d3=KmToGD(r3)
    A=pow(x1,2)+pow(y1,2)-pow(d1,2)
    B=pow(x2,2)+pow(y2,2)-pow(d2,2)
    C=pow(x3,2)+pow(y3,2)-pow(d3,2)
    X32=x3-x2
    X13=x1-x3
    X21=x2-x1
    Y32=y3-y2
    Y13=y1-y3
    Y21=y2-y1
    x=((A*Y32)+(B*Y13)+(C*Y21))/(2*((x1*Y32)+(x2*Y13)+(x3*Y21)))
    y=((A*X32)+(B*X13)+(C*X21))/(2*((y1*X32)+(y2*X13)+(y3*X21)))
    return y,x
