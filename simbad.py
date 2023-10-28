import requests
import os
import re

databaseSearchUri="https://simbad.cds.unistra.fr/simbad/sim-id?output.format=ASCII&coodisp1=d&frame1=ICRS&Ident="

def LoadDataFor(name):
    with requests.Session() as session:
        response=session.get(databaseSearchUri + name) #MUST be GET request as with Celestrack.
        if response.status_code != 200:
            print(response)
            exit()
        data=response.text
        lines=data.split("\n")
        alpha=delta=mu_alpha=mu_delta=0
        for line in lines:
            if line.startswith("Coordinates(ICRS,ep=J2000,eq=2000):"):
                coordinates=line[(line.find(":")+len(":")):(line.rfind("("))]
                values=coordinates.split()
                alpha=float(values[0].strip())
                delta=float(values[1].strip())
            if line.startswith("Proper motions:"):
                properMotions=line[(line.find(":")+len(":")):(line.rfind("["))]
                values=properMotions.split()
                mu_alpha=float(values[0].strip())
                mu_delta=float(values[1].strip())
        return alpha,delta,mu_alpha,mu_delta

def LoadHPIdFor(name):
    with requests.Session() as session:
        response=session.get(databaseSearchUri + name) #MUST be GET request as with Celestrack.
        if response.status_code != 200:
            print(response)
            exit()
        data=response.text
        lines=data.split("\n")
        hpId=0
        for line in lines:
            if line.startswith("   HIP"):
                value=line[(line.find("P")+len("P")):(line.find("P")+len("P")+15)]
                hpId=int(value.strip())
        return hpId
