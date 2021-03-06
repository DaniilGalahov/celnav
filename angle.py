#auxilliary functions to deal with angular coordinates
import re
import math

def ToDecimal(value):
    if isinstance(value, str):
        dmsd = re.split('[^\d\w.]+', value) #only for strings like "157°25.6' S"
        
        value = float(dmsd[0]) + (float(dmsd[1])/60.0);
    
        if dmsd[2] == 'W' or dmsd[2] == 'S':
            value *= -1
        
    return value


def Normalize(value):
    negative=False
    if value<0.0:
        negative=True
        
    value=math.fabs(value)
    
    if value>360:
        value=value%360

    if negative:
        value=360.0-value

    return value


def ToString(value):
    value=Normalize(value)

    d=int(value)    
    md=(value-float(d))*60.0
    
    if math.isclose(md,60.0,rel_tol=0.016):
        d+=1
        md=0.0
	
    strD=str(d)
    strMd=str(round(md,2))
	
    if md<10:
        strMd="0"+strMd
    
    return strD+"°"+strMd+"'"


def ToLatitude(value):
    sine=math.sin(math.radians(value))
    value=math.degrees(math.asin(sine))

    direction="N"
    if value<0.0:
        direction="S"
    
    return ToString(math.fabs(value))+" "+direction


def ToLongtitude(value):
    if value>180.0:
        value=value%360
        delta=value-180.0
        value=180.0-delta
        value*=-1.0

    direction="E"
    if value<0.0:
        direction="W"
    
    cosine=math.cos(math.radians(value))
    value=math.degrees(math.acos(cosine))

    return ToString(math.fabs(value))+" "+direction
