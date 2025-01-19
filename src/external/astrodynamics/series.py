#set of functions for series calculation
from .external.math import *

def PowerSeries(x, coefficients):
    result=0
    for n in range(len(coefficients)):
        result+=coefficients[n]*pow(x,n)
    return result

def MoonSinSeries(x, coefficients):
    result=0
    for n in range(len(coefficients)):
        a=coefficients[n][0]
        b=coefficients[n][1]
        c=coefficients[n][2]
        result+=a*sin(radians(b+(c*x)))
    return result

def MoonCosSeries(x, coefficients):
    result=0
    for n in range(len(coefficients)):
        a=coefficients[n][0]
        b=coefficients[n][1]
        c=coefficients[n][2]
        result+=a*cos(radians(b+(c*x)))
    return result
