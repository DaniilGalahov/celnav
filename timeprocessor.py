#time functions for navigational applications
import re
import angle

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

def ToAstropyTimeString(date, time):
    ddmmyyyy=re.split('[^\d]+', date)
    hhmm=re.split('[^\d]+', time)
    return ddmmyyyy[2]+"-"+ddmmyyyy[1]+"-"+ddmmyyyy[0]+" "+hhmm[0]+":"+hhmm[1]

def HoursToSeconds(hours):
    return hours*60*60

def SecondsToHours(seconds):
    return seconds/(60.0*60.0)

def ExactTimeZone(L):
    longtitude=angle.ToDecimal(L)
    return longtitude/(360/24)

def TimeZone(L):
    return int(ExactTimeZone(L))
