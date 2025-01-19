#utility for read data from Vallado CIP tables
from .external.modules import *

dataDirectoryName="data"

def AbsolutePathFor(subDirectoryName,fileName):
    absolutePathForRootDirectory = os.path.dirname(os.path.abspath(__file__))
    absolutePathForFile=os.path.join(absolutePathForRootDirectory,subDirectoryName,fileName)
    return absolutePathForFile

def ReadOrbitalElementCoefficients(fileName):
    def Convert(line):
        substrings=line.split(",")
        terms=[]
        for substring in substrings:
            terms.append(float(substring))
        return terms
    file = open(AbsolutePathFor(dataDirectoryName,fileName),"r")
    lines = file.readlines()
    file.close()
    coefficients_a=Convert(lines[0])
    coefficients_e=Convert(lines[1])
    coefficients_i=Convert(lines[2])
    coefficients_Omega=Convert(lines[3])
    coefficients__omega=Convert(lines[4])
    coefficients_lambdaM=Convert(lines[5])
    return(coefficients_a,coefficients_e,coefficients_i,coefficients_Omega,coefficients__omega,coefficients_lambdaM)
