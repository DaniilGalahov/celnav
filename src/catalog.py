#Star catalog interface
from external.modules import *

import simbad
import hipparcos

navigationStarNames=["Acamar",
                     "Achernar",
                     "Acrux",
                     "Adhara",
                     "Albireo",
                     "Aldebaran",
                     "Alioth",
                     "Alkaid",
                     "Al Na-ir",
                     "Alnilam",
                     "Alphard",
                     "Alphecca",
                     "Alpheratz",
                     "Altair",
                     "Ankaa",
                     "Antares",
                     "Arcturus",
                     "Atria",
                     "Avior",
                     "Bellatrix",
                     "Betelgeuse",
                     "Canopus",
                     "Capella",
                     "Castor",
                     "Deneb",
                     "Denebola",
                     "Diphda",
                     "Dubhe",
                     "Elnath",
                     "Eltanin",
                     "Enif",
                     "Fomalhaut",
                     "Gacrux",
                     "Gienah",
                     "Hadar",
                     "Hamal",
                     "Kochab",
                     "Markab",
                     "Menkar",
                     "Menkent",
                     "Miaplacidus",
                     "Mirfak",
                     "Nunki",
                     "Peacock",
                     "Polaris",
                     "Pollux",
                     "Procyon",
                     "Rasalhague",
                     "Regulus",
                     "Rigel",
                     "Sabik",
                     "Schedar",
                     "Shaula",
                     "Sirius",
                     "Spica",
                     "Suhail",
                     "Vega",
                     "Zuben-ubi"]

dataSource=0 #0 - Hipparcos, 1 - SIMBAD
dataDirectoryName="Data"
catalogFileName="catalog.dat"

def AbsolutePathFor(subDirectoryName,fileName):
    absolutePathForRootDirectory = os.path.dirname(os.path.abspath(__file__))
    absolutePathForFile=os.path.join(absolutePathForRootDirectory,subDirectoryName,fileName)
    return absolutePathForFile

def LoadDataFromSourceFor(name):
    nameInSource=name
    if name=="Al Na-ir":
        nameInSource="Alpha+Gruis"
    if name=="Zuben-ubi":
        nameInSource="Alpha+Librae"
    alpha=delta=mu_alpha=mu_delta=0
    if dataSource==0:
        hpId=simbad.LoadHPIdFor(nameInSource)
        alpha,delta,mu_alpha,mu_delta=hipparcos.LoadDataFor(hpId)
    if dataSource==1:
        alpha,delta,mu_alpha,mu_delta=simbad.LoadDataFor(nameInSource)
    if alpha==0 and delta==0 and mu_alpha==0 and mu_delta==0:
        print("Coordinate data loading for "+name+" failed.")
    else:
        print("Loaded coordinate data for "+name+".")
    return alpha,delta,mu_alpha,mu_delta

def CreateLocalCatalog():
    records={}
    for navigationStarName in navigationStarNames:
        alpha,delta,mu_alpha,mu_delta=LoadDataFromSourceFor(navigationStarName)
        records[navigationStarName]=(alpha,delta,mu_alpha,mu_delta)
    jsonString=json.dumps(records)
    file=open(AbsolutePathFor(dataDirectoryName,catalogFileName),"w")
    file.write(jsonString)
    file.close()
    print("Catalog data saved")

def LoadDataFor(name):
    alpha=delta=mu_alpha=mu_delta=0
    file=open(AbsolutePathFor(dataDirectoryName,catalogFileName),"r")
    data=file.read()
    file.close()
    records=json.loads(data)    
    if name in records:
        alpha,delta,mu_alpha,mu_delta=records[name]
    return alpha,delta,mu_alpha,mu_delta

if __name__ == '__main__':
    if os.path.exists(AbsolutePathFor(dataDirectoryName,catalogFileName)):
        print("Local catalog file exists.")
    else:
        print("Local catalog file NOT exists.")
    answer=input("Create new catalog from external source? (y/n) ")
    if answer=="y":
        answer=input("From what source? (0 - Hipparchos, 1 - SIMBAD) ")
        if answer=="0" or answer=="1":
            dataSource=int(answer)
            CreateLocalCatalog()
            print("Local catalog created.")
    input("Input any symbol to exit...")  
