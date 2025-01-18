#Functions to work with route
from external.math import *
from external.astro import *

def DR(phi0,lambda0,V,Vdir,D,Ddir,dt): #initial lat, initial lon, speed (km/h), speed direction (d.d.), drift (km/h), drift direction (d.d.), delta time (h)
    def KmToGD(x):
        return x/1.852/60.0
    vector_Tv=dot(ROT3(radians(Vdir)),vector([0,1,0])*KmToGD(V)*dt)
    vector_Td=dot(ROT3(radians(Ddir)),vector([0,1,0])*KmToGD(D)*dt)
    vector_T=vector_Tv+vector_Td
    vector_P0=vector([lambda0,phi0,0])
    vector_P1=vector_P0+vector_T
    phi1=vector_P1[1]
    lambda1=vector_P1[0]
    return phi1,lambda1
    
    
