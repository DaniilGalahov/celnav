from external.math import *
from external.astro import *

from astrometry import AzElFor
import angle

def COZCorrection(magHdg,phi,lambda_,Y,M,D,h,m,s,celestialObjectName,celestialObjectAz):
    az,el=AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s)
    corr=-(celestialObjectAz-az)
    trueHdg=angle.Normalize(magHdg+corr)
    return trueHdg,corr

def POZCorrection(magHdg,phiPos,lambdaPos,phiObj,lambdaObj,azObj):
    vector_N=vector([0,1,0])
    vector_PO=vector([lambdaObj,phiObj,0])-vector([lambdaPos,phiPos,0])
    vector_D=vector([0,0,-1])
    signedAzObj=angle.ToSigned180(azObj)
    signedAzPos=signedAngleBetween(vector_N,vector_PO,vector_D)
    corr=-(signedAzObj-signedAzPos)
    trueHdg=angle.Normalize(magHdg+corr)
    return trueHdg,corr
    
