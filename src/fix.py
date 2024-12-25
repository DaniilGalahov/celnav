from external.math import sin, cos, degrees, radians
import equationsolver as solve

def Fix(phigce,lambdae,p1,z1,p2,z2):
    x,y=solve.LinEq22(sin(radians(z1)),cos(radians(z1)),p1,sin(radians(z2)),cos(radians(z2)),p2)
    phigc=phigce+(y/60.0)    
    lambda_=lambdae+(x/60.0/cos(radians(phigc)))
    return phigc,lambda_

def OneObjectTwoFix(phigce,lambdae,p1,z1,p2,z2,dt,hdg=0,v=0):
    D=v*dt
    p1=p1+(D*cos(radians(hdg)-radians(z1)))
    return Fix(phigce,lambdae,p1,z1,p2,z2)

def TwoObjectFix(phigce,lambdae,p1,z1,p2,z2):
    return Fix(phigce,lambdae,p1,z1,p2,z2)

def ThreeObjectFix(phigce,lambdae,p1,z1,p2,z2,p3,z3):
    phigc1,lambda1=Fix(phigce,lambdae,p1,z1,p2,z2)
    phigc2,lambda2=Fix(phigce,lambdae,p2,z2,p3,z3)
    phigc3,lambda3=Fix(phigce,lambdae,p3,z3,p1,z1)
    phigc=(phigc1+phigc2+phigc3)/3.0
    lambda_=(lambda1+lambda2+lambda3)/3.0
    return phigc,lambda_
    
        
