#constants library and wrapper for usage astropy.constants in algorithms from Vallado books
from .external.astro import *

unitOfLength=u.km
unitOfTime=u.s

'''
def PrintDefaultUnits():
    print("Default unit of length is "+str(unitOfLength)+".")
    print("Default unit of time is "+str(unitOfTime)+".")
'''

def muEarthAstropy():
    return (astropy.constants.G * astropy.constants.M_earth).to((unitOfLength**3)/(unitOfTime**2)).value

def muEarthVallado():
    return (398600.4418*((unitOfLength**3)/(unitOfTime**2))).value

def muSunWiki(): #from https://en.wikipedia.org/wiki/Standard_gravitational_parameter
    return ((1.32712440018e+20)*((u.m**3)/(u.s**2))).to((unitOfLength**3)/(unitOfTime**2)).value

def muSunVallado():
    return ((1.32712428e+11)*((u.km**3)/(u.s**2))).to((unitOfLength**3)/(unitOfTime**2)).value

mu=muEarthVallado()

def REarthAstropy():
    return astropy.constants.R_earth.to(unitOfLength).value

def REarthVallado():
    return (6378.137*unitOfLength).value

Rearth=REarthVallado()

eearth=0.081819221456 #Earth eccentricity from Vallado

omegaearth=0.0000729211585530 #Earth rotation rate from Vallado

def AUWiki():
    return (1.495978707e+8*unitOfLength).value #AU from english Wikipedia

AU=AUWiki()

def MEarthVallado():
    return 5.9733328e+24

def MEarthAstropy():
    return astropy.constants.M_earth.value

Mearth=MEarthAstropy()

def GAstropy(): #Gravitational constant
    return astropy.constants.G.value

G=GAstropy()
