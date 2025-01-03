from external.math import *
from external.astro import *

def IJK2SEZ(vector_rIJK,phi,thetaLST):
    return dot(ROT2(radians(90.0-phi))@ROT3(radians(thetaLST)),vector_rIJK)
