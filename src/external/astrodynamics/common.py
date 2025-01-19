#common functions
def NormalizeInRange(x,rangeMin,rangeMax):
    length=abs(rangeMax-rangeMin)
    signedRemaider=x%length
    if x<0:
        signedRemaider=x%-length
    value=rangeMin+signedRemaider
    if value<rangeMin:
        value=rangeMax-abs(value)
    return value

def ToSignedAngle(x):
    remainder=x%360.0
    value=remainder
    if remainder>180.0:
        value=-180.0+(abs(remainder)-180.0)
    if remainder<-180.0:
        value=180.0-(abs(remainder)-180.0)
    return value
