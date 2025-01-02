#time functions for navigational applications
from external.modules import re
from external.astro import JulianDate, JDtoGregorianDate
import angle

def APyTimeToYMDhms(aPyTime):
    YMDhms=re.split('[^\d^.]+', aPyTime)
    Y=int(YMDhms[0])
    M=int(YMDhms[1])
    D=int(YMDhms[2])
    h=int(YMDhms[3])
    m=int(YMDhms[4])
    s=0
    if len(YMDhms)>5:
        s=round(float(YMDhms[5]),3)
    return Y,M,D,h,m,s

def YMDhmsToAPyTime(Y,M,D,h,m,s):
    return "{0:0>4n}-{1:0>2n}-{2:0>2n} {3:0>2n}:{4:0>2n}:{5:0>6.3f}".format(Y,M,D,h,m,s)    

def DateTimeToYMDhms(dateString, timeString):
    ddmmyyyy=re.split('[^\d]+', dateString)
    hhmm=re.split('[^\d]+', timeString)
    Y=int(ddmmyyyy[2])
    M=int(ddmmyyyy[1])
    D=int(ddmmyyyy[0])
    h=int(hhmm[0])
    m=int(hhmm[1])
    s=0
    return Y,M,D,h,m,s

def ToSeconds(string):
    if isinstance(string, str):
        hhmmsss = re.split('[^\d]+', string)
        seconds=0
        if len(hhmmsss)>0:
            seconds=(int(hhmmsss[0])*60*60)
        if len(hhmmsss)>1:
            seconds+=(int(hhmmsss[1])*60)
        if len(hhmmsss)>2:
            seconds+=(float(hhmmsss[2]))
    return seconds

def ToString(seconds):
    h=int(seconds//3600)
    m=int((seconds//60)-(h*60))
    s=seconds-((h*60*60)+(m*60))
    string="{0:0>2n}:{1:0>2n}:{2:0>6.3f}".format(h,m,s)
    return string

def ExactTimeZone(L):
    longitude=angle.ToDecimal(L)
    return longitude/(360/24)

def TimeZone(L):
    return round(ExactTimeZone(L))

def LTtoGMT(Y,M,D,h,m,s,lambda_):
    JDGMT=JulianDate(Y,M,D,h,m,s)
    timeZone=TimeZone(lambda_)
    JDOffset=(timeZone*3600)/86400.0
    JDUTC=JDGMT-JDOffset
    return JDtoGregorianDate(JDUTC)
