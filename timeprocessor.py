#time functions for navigational applications
import re
import angle

def ToSeconds(value):
    if isinstance(value, str):
        hhmm = re.split('[^\d]+', value)
        value=(int(hhmm[0])*60*60)+(int(hhmm[1])*60)
        
    return value


def ToString(seconds):
    hh=int(seconds/(60*60))
    mm=int((seconds-(hh*60*60))/60)

    hh=str(hh)
    mm=str(mm)

    if len(mm)<2:
        mm="0"+mm
    
    return hh+":"+mm

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


def AdditionalGMTOffset(L): #not required - we counting this offset as LHA in intercept algorithm
    exactTimeZone=ExactTimeZone(L)
    timeZone=TimeZone(L)
    additionalGMTOffset=HoursToSeconds(exactTimeZone-timeZone)

    return additionalGMTOffset
