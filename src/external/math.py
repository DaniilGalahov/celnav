#math
from math import sqrt, fabs, ceil, sin, cos, tan, asin, acos, atan, atan2, degrees, radians, pi, isclose

#numpy
from numpy import array as vector, cross, dot
from numpy.linalg import norm as magnitude

def sign(x):
    if x<0:
        return -1
    else:
        return 1
