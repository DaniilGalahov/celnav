import requests
import os

databaseSearchUri="https://hipparcos-tools.cosmos.esa.int/cgi-bin/HIPcatalogueSearch.pl?hipId="

def LoadDataFor(hpId):
    with requests.Session() as session:
        response=session.get(databaseSearchUri + str(hpId)) #MUST be GET request as with Celestrack.
        if response.status_code != 200:
            print(response)
            exit()
        data=response.text
        lines=data.split("\n")
        alpha=delta=mu_alpha=mu_delta=0
        for line in lines:
            if line.startswith("H8  :"):
                alpha=float(line[6:27].strip())
            if line.startswith("H9  :"):
                delta=float(line[6:27].strip())
            if line.startswith("H12 :"):
                mu_alpha=float(line[6:27].strip())
            if line.startswith("H13 :"):
                mu_delta=float(line[6:27].strip())
        return alpha,delta,mu_alpha,mu_delta
    
