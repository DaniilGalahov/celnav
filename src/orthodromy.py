#Orthodromy algorithms
#Based on description in Wiki: https://en.wikipedia.org/wiki/Great-circle_navigation
#Additional info: https://en.wikipedia.org/wiki/Geodesics_on_an_ellipsoid
from external.math import *

from celestialobject import Rearth
import angle

def Between2Pos(phi1,lambda1,phi2,lambda2,R=Rearth): #point1 (start) phi, point1 (start) lambda, point2 (destination) phi, point2 (destination) lambda, planet radius; #this realisation is for spherical Earth (not for ellipsoid)
    phi1=radians(phi1)
    lambda1=radians(lambda1)
    phi2=radians(phi2)
    lambda2=radians(lambda2)
    lambda12=lambda2-lambda1
    alpha1=atan2(cos(phi2)*sin(lambda12), (cos(phi1)*sin(phi2))-(sin(phi1)*cos(phi2)*cos(lambda12))) #heading at start
    alpha2=atan2(cos(phi1)*sin(lambda12),(-cos(phi2)*sin(phi1))+(sin(phi2)*cos(phi1)*cos(lambda12))) #heading at destination
    delta12=atan2(sqrt(pow((cos(phi1)*sin(phi2))-(sin(phi1)*cos(phi2)*cos(lambda12)),2)+pow(cos(phi2)*sin(lambda12),2)),(sin(phi1)*sin(phi2))+(cos(phi1)*cos(phi2)*cos(lambda12))) #angular length of arc of great circle
    s12=R*delta12  #actual length of arc of great-circle (orthodromic distance)
    return angle.Normalize(degrees(alpha1)),angle.Normalize(degrees(alpha2)),degrees(delta12),s12

def PointHdg(phi1,lambda1,alpha1,d,R=Rearth): #point1 phi, point1 lambda, heading, distance (km), planet radius; #this realisation is for spherical Earth (not for ellipsoid)
    phi1=radians(phi1)
    lambda1=radians(lambda1)
    alpha1=radians(alpha1)
    alpha0=atan2(sin(alpha1)*cos(phi1),sqrt(pow(cos(alpha1),2)+(pow(sin(alpha1),2)*pow(sin(phi1),2))))
    if phi1==0 and alpha1==pi/2:
        delta01=0.0
    else:
        delta01=atan2(tan(phi1),cos(alpha1))
    delta12=d/R
    delta=delta01+delta12
    lambda01=atan2(sin(alpha0)*sin(delta01),cos(delta01))
    lambda0=lambda1-lambda01
    phi2=atan2(cos(alpha0)*sin(delta),sqrt(pow(cos(delta),2)+(pow(sin(alpha0),2)*pow(sin(delta),2))))
    lambda2=atan2(sin(alpha0)*sin(delta),cos(delta))+lambda0
    alpha2=atan2(tan(alpha0),cos(delta))
    return angle.ToSigned180(degrees(phi2)),angle.ToSigned180(degrees(lambda2)),angle.Normalize(degrees(alpha2))
