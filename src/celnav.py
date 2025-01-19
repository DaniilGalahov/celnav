#High-level access to algorithms of library
from timeprocessor import LTtoGMT
from astrometry import ElevationCorrection, FindToCoEE
from position import FromToCoEEo2CO, FromToCoEEo3CO, FromP3A3, FromP3R3
from orthodromy import Between2Pos, PointHdg
from compass import COZCorrection, POZCorrection
from route import DR
from angle import ToDecimal

#1) Detecting GMT
def LTToGMT(Y,M,D,h,m,s,lambdaAP):
    return LTtoGMT(Y,M,D,h,m,s,lambdaAP)

#2) Detect current position
def SightReduction(phiAP,lambdaAP,Y,M,D,h,m,s,celestialObjectName,el,indexCorrection=0,hoe=0,T=10,P=1010.0,limb=0):
    el=el+ElevationCorrection(celestialObjectName,Y,M,D,h,m,s,el,indexCorrection,hoe,T,P,limb)
    return FindToCoEE(phiAP,lambdaAP,Y,M,D,h,m,s,celestialObjectName,el)

def TwoObjectFix(phiAP,lambdaAP,a1,Z1,a2,Z2):
    return FromToCoEEo2CO(phiAP,lambdaAP,a1,Z1,a2,Z2)

def ThreeObjectFix(phiAP,lambdaAP,a1,Z1,a2,Z2,a3,Z3):
    return FromToCoEEo3CO(phiAP,lambdaAP,a1,Z1,a2,Z2,a3,Z3)

def ThreeAnglesFix(phi1,lambda1,phi2,lambda2,phi3,lambda3,alpha12,alpha23,alpha31):
    return FromP3A3(phi1,lambda1,phi2,lambda2,phi3,lambda3,alpha12,alpha23,alpha31)

def ThreeRangesFix(phi1,lambda1,phi2,lambda2,phi3,lambda3,r1,r2,r3):
    return FromP3R3(phi1,lambda1,phi2,lambda2,phi3,lambda3,r1,r2,r3)

#3) Detect required heading
def Orthodromy(phi1,lambda1,phi2,lambda2):
    return Between2Pos(phi1,lambda1,phi2,lambda2)

def HeadingAtWaypoint(phi1,lambda1,alpha1,d):
    return PointHdg(phi1,lambda1,alpha1,d)

#4) Calculate compass heading
def CompassCorrectionCOZ(magHdg,phi,lambda_,Y,M,D,h,m,s,celestialObjectName,celestialObjectAz):
    return COZCorrection(magHdg,phi,lambda_,Y,M,D,h,m,s,celestialObjectName,celestialObjectAz)

def CompassCorrectionPOZ(magHdg,phiPos,lambdaPos,phiObj,lambdaObj,azObj):
    return POZCorrection(magHdg,phiPos,lambdaPos,phiObj,lambdaObj,azObj)
    
#5) Calculate passed route
def DeadReckoning(phi0,lambda0,V,Vdir,D,Ddir,dt):
    return DR(phi0,lambda0,V,Vdir,D,Ddir,dt)

#6) Auxilliary functions
def AngleToDecimal(string):
    return ToDecimal(string)
