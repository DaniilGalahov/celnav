#Interface of Hipparchos online astronomical catalog
from external.modules import *

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
            match=re.search("H8\s*:\s*(\W*\d*\.*\d*)",line)
            if match is not None:
                alpha=float(match.group(1).strip())
                continue
            match=re.search("H9\s*:\s*(\W*\d*\.*\d*)",line)
            if match is not None:
                delta=float(match.group(1).strip())
                continue
            match=re.search("H12\s*:\s*(\W*\d*\.*\d*)",line)
            if match is not None:
                mu_alpha=float(match.group(1).strip())
                continue
            match=re.search("H13\s*:\s*(\W*\d*\.*\d*)",line)
            if match is not None:
                mu_delta=float(match.group(1).strip())
                continue
        return alpha,delta,mu_alpha,mu_delta
