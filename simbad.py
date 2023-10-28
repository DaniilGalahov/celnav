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
            match=re.search("Coordinates\(ICRS,ep=J2000,eq=2000\):\s*(\W*\d*\.*\d*)\s*(\W\d*\.*\d*)",line)
            if match is not None:
                alpha=float(match.group(1).strip())
                delta=float(match.group(2).strip())
            match=re.search("Proper motions:\s*(\W*\d*\.*\d*)\s*(\W\d*\.*\d*)",line)
            if match is not None:
                mu_alpha=float(match.group(1).strip())
                mu_delta=float(match.group(2).strip())
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
            match=re.search("HIP\s*(\d*)",line)
            if match is not None:
                hpId=int(match.group(1).strip())
        return hpId
