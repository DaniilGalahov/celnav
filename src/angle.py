#auxilliary functions to deal with angular coordinates
from external import re, fabs, sin, cos, tan, asin, acos, degrees, radians, isclose

def ToDecimal(value):
    if isinstance(value, str):
        #[NSEW] regex for direction
        #[-\d]+\* regex for getting degrees only
        #[\d.]+' regex for getting decimal minutes only
        #[-\d.]+ regex for signed digits and decimal point only
        value = value.replace("°","*")
        value = value.replace(",",".")
        directionPattern=re.compile("[NSEW]")
        directionStrings = directionPattern.findall(value)
        degreesPattern=re.compile("[-\d]+\*")
        degreesStrings=degreesPattern.findall(value)
        minutesPattern=re.compile("[\d.]+'")
        minutesStrings=minutesPattern.findall(value)
        decimalPattern=re.compile("[-\d.]+")
        decimalStrings=decimalPattern.findall(value)
        if len(degreesStrings)>0 and len(minutesStrings)>0:
            degrees=float(decimalPattern.findall(degreesStrings[0])[0])
            sign=1.0
            if degrees<0:
                sign=-1.0            
            minutes=sign*float(decimalPattern.findall(minutesStrings[0])[0])            
            value = degrees+(minutes/60.0)
        elif len(decimalStrings)>0:
            value = float(decimalStrings[0])
        direction=""
        if len(directionStrings)>0:
            direction=directionStrings[0]    
        if direction == 'W' or direction == 'S':
            value *= -1        
    return value

def ToSigned180(value):
    value = value%360    
    if value>180.0:
        delta=value-180.0
        value=180.0-delta
        value*=-1.0
    return value

def Normalize(value):
    negative=False
    if value<0.0:
        negative=True        
    value=fabs(value)    
    if value>360:
        value=value%360
    if negative:
        value=360.0-value
    return value

def ToString(value):
    value=Normalize(value)
    d=int(value)    
    md=(value-float(d))*60.0    
    if isclose(md,60.0,rel_tol=0.016):
        d+=1
        md=0.0	
    strD=str(d)
    strMd=str(round(md,2))	
    if md<10:
        strMd="0"+strMd    
    return strD+"°"+strMd+"'"

def ToJSONCompatible(string):
    return string.replace("°","*")

def ToLatitude(value):
    sine=sin(radians(value))
    value=degrees(asin(sine))
    direction="N"
    if value<0.0:
        direction="S"    
    return ToString(fabs(value))+" "+direction

def ToLongtitude(value):
    value=ToSigned180(value)
    direction="E"
    if value<0.0:
        direction="W"    
    cosine=cos(radians(value))
    value=degrees(acos(cosine))
    return ToString(fabs(value))+" "+direction
