#local version of astrodynamic algorithms from Vallado book (to make library independent)
#THIS IS VERY IMPORTANT EXAMPLE OF HOW TO REFACTOR ASTRODYNAMICS LIBRARY
from .external.math import *

from .series import PowerSeries, MoonSinSeries, MoonCosSeries
from .common import NormalizeInRange
from .frames import IJK
from .datareader import ReadOrbitalElementCoefficients
from .constants import Rearth, eearth, omegaearth, mu, AU, muSunWiki
from .math import ROT1, ROT2, ROT3, angle, signedAngle

def ConvTime(yr,mo,day,UTC,deltaUT1,deltaAT):
    def Series(x, coefficients): #series term is (c1*sin((c2*TTT)+c3))
        result=0
        for n in range(len(coefficients)):
            a=coefficients[n][0]
            b=coefficients[n][1]
            c=coefficients[n][2]
            result+=a*sin((b*x)+c)
        return result
    UT1=UTC+deltaUT1 #UT1
    hUT1,min_UT1,sUT1=TimeToHMS(UT1)
    JDUT1=JulianDate(yr,mo,day,hUT1,min_UT1,sUT1)
    TUT1=(JDUT1-2451545.0)/36525 #TUT1
    TAI=UTC+deltaAT #TAI
    GPS=UTC+deltaAT-19 #GPS
    TT=TAI+32.184 #TT
    hTT,min_TT,sTT=TimeToHMS(TT)
    JDTT=JulianDate(yr,mo,day,hTT,min_TT,sTT)
    TTT=(JDTT-2451545.0)/36525 #TTT
    TDB=TT+Series(TTT,[[0.001657,628.3076,6.2401],[0.000022,575.3385,4.2970],[0.000014,1256.6152,6.1969],[0.000005,606.9777,4.0212],[0.000005,52.9691,0.4444],[0.000002,21.3299,5.5431],[0.000010,628.3076,4.2490]]) #TDB
    hTDB,min_TDB,sTDB=TimeToHMS(TDB)
    JDTDB=JulianDate(yr,mo,day,hTDB,min_TDB,sTDB)
    TTDB=(JDTDB-2451545.0)/36525 #TTDB
    hTAI,min_TAI,sTAI=TimeToHMS(TAI)
    JDTAI=JulianDate(yr,mo,day,hTAI,min_TAI,sTAI)
    t0=2443144.5 #in JDTAI, in UTC Jan 1, 1977, 00:00:00.000
    TCB=TT+(1.55051976772*pow(10,-8)*((JDTAI-t0)*86400)) #TCB
    Lg=6.969290134*pow(10,-10) #scale constant to account gravitational and rotational potential of Earth
    TCG=TT+((Lg/(1-Lg))*((JDTT-t0)*86400)) #TCG
    return UT1,TAI,GPS,TT,TDB,TCB,TCG,TUT1,TTT,TTDB

def JulianDate(yr,mo,d,h,min_,s): #1900 to 2100
    return (367*yr)-int((7*(yr+int((mo+9)/12)))/4)+int((275*mo)/9)+d+1721013.5+(((((s/60)+min_)/60)+h)/24)

def JDtoGregorianDate(JD):
    T1900=(JD-2415019.5)/365.25
    Year=1900+trunc(T1900)
    LeapYrs=trunc((Year-1900-1)*0.25)
    Days=(JD-2415019.5)-(((Year-1900)*365)+LeapYrs)
    if Days<1.0:
        Year=Year-1
        LeapYrs=trunc((Year-1900-1)*0.25)
        Days=(JD-2415019.5)-(((Year-1900)*365)+LeapYrs)
    DayOfYr=trunc(Days)
    Year,Mon,Day = DayOfYearToYMD(Year, DayOfYr)
    tau=(Days-DayOfYr)*86400
    h,min_,s=TimeToHMS(tau)
    return Year,Mon,Day,h,min_,s

def LSTime(JDUT1,UT1,lambda_): #Original version from Vallado book (Algorithm #15), UT1 argument not used (probably error?); Correct input is "JD, 0, lambda"
    TUT1=(JDUT1-2451545.0)/36525
    #thetaGMST=67310.54841+(((876600*3600)+8640184.812866)*TUT1)+(0.093104*pow(TUT1,2))-(6.2*pow(10,-6)*pow(TUT1,3)) #from original formula (Vallado eq. 3-47)
    thetaGMST=PowerSeries(TUT1,[43200+24110.54841,(876600*3600)+8640184.812866,0.093104,-6.2*1e-6]) #first subterm of second term of expression are in hours, so for convert into seconds we must multiple it by 3600;
    thetaGMST=(NormalizeInRange(thetaGMST,0,86400))/240 #reducing seconds to one day and converting them to degrees
    if thetaGMST<0:
        thetaGMST=360+thetaGMST
    thetaLST=thetaGMST+lambda_
    return thetaLST,thetaGMST

def HMSToTime(h,m,s):
    return (h*3600)+(m*60)+s

def TimeToHMS(tau):
    temp=tau/3600
    h=trunc(temp)
    min_=trunc((temp-h)*60)
    s=(temp-h-(min_/60))*3600
    return h,min_,s

def DayOfYearToYMD(y, dayOfYear):
    monthsLength=MonthsLengthFor(y)
    temp=0
    currentMonth=0
    while True:
        temp+=monthsLength[currentMonth]
        if temp>dayOfYear:
            break
        currentMonth+=1
        if currentMonth==len(monthsLength):
            currentMonth=currentMonth-1
            break
    temp-=monthsLength[currentMonth]
    m=currentMonth+1
    d=dayOfYear-temp
    return y,m,d

def MonthsLengthFor(y): #valid only for years 1900-2100, because don't count leap years centuries dividable by 400 (more in Vallado, chapter 3.6.4)
    monthsLength=[31,28,31,30,31,30,31,31,30,31,30,31]
    if y%4==0:
        monthsLength[1]=29
    return monthsLength

def KepEqtnE(M,e):
    M=radians(M) #For correct calculations M must be in radians!
    if -pi<M<0 or pi<M<2*pi: #correction from Errata V4
        Einit=M-e
    else:
        Einit=M+e
    Ecurr = Einit
    Enext = inf
    while True:
        Enext=Ecurr+((M-Ecurr+(e*sin(Ecurr))))/(1-(e*cos(Ecurr)))
        if abs(Enext-Ecurr)<pow(10,-8):
            break;
        Ecurr=Enext
    return degrees(Enext)

def Anomalytonu(e, E, B, p, r, H):
    if e<1:
        E=radians(E) #For correct calculations E must be in radians!
        sinnu=(sin(E)*sqrt(1-pow(e,2)))/(1-(e*cos(E)))
        cosnu=(cos(E)-e)/(1-(e*cos(E)))
    if e==1:
        sinnu=(p*B)/r
        cosnu=(p-r)/r
    if e>1:
        sinnu=(-sinh(H)*sqrt(pow(e,2)-1))/(1-(e*cosh(H)))
        cosnu=(cosh(H)-e)/(1-(e*cosh(H)))
    nu=atan2(sinnu, cosnu)
    return degrees(nu)

def COE2RV(p,e,i,Omega,omega,nu,u,lambdatrue,_omegatrue):
    def CircularEquatorial(e,i,elim=0.00014990256333383302,ilim=0.008588784249387266): #default values for Earth
        isMatch=False
        if abs(e)<=elim and abs(i)<=ilim:
            isMatch=True
        return isMatch
    def CircularInclined(e,i,elim=0.00014990256333383302,ilim=0.008588784249387266):
        isMatch=False
        if abs(e)<=elim and abs(i)>ilim:
            isMatch=True
        return isMatch
    def EllipticalEquatorial(e,i,elim=0.00014990256333383302,ilim=0.008588784249387266):
        isMatch=False
        if abs(e)>elim and abs(i)<=ilim:
            isMatch=True
        return isMatch
    i=radians(i)
    Omega=radians(Omega)
    omega=radians(omega)
    nu=radians(nu)
    if CircularEquatorial(e,i):
        lambdatrue=radians(lambdatrue)
        omega=Omega=0
        nu=lambdatrue
    if CircularInclined(e,i):
        u=radians(u)
        omega=0
        nu=u
    if EllipticalEquatorial(e,i):
        _omegatrue=radians(_omegatrue)
        Omega=0
        omega=_omegatrue
    vector_rPQW=vector([(p*cos(nu))/(1+(e*cos(nu))), (p*sin(nu))/(1+(e*cos(nu))), 0])
    vector_vPQW=vector([-sqrt(mu/p)*sin(nu), sqrt(mu/p)*(e+cos(nu)), 0])
    vector_rIJK=dot(ROT3(-Omega)@ROT1(-i)@ROT3(-omega),vector_rPQW) # @ is matrix multiplication - same as matmul in Orbiter
    vector_vIJK=dot(ROT3(-Omega)@ROT1(-i)@ROT3(-omega),vector_vPQW)
    return vector_rIJK, vector_vIJK

def GeocentricRadec(vector_rIJK,vector_vIJK):
    r=magnitude(vector_rIJK)
    repl=sqrt(pow(vector_rIJK[IJK.axis.I],2)+pow(vector_rIJK[IJK.axis.J],2)) #length of projection of vector_rIJK to equatorial plane; NB!!! For correct calculation of pow(x,y) we must use only floating point numbers!
    delta=atan2(vector_rIJK[IJK.axis.K]/r,repl/r)
    if repl != 0:
        alpha=atan2(vector_rIJK[IJK.axis.J]/repl,vector_rIJK[IJK.axis.I]/repl)
    else:
        vepl=sqrt(pow(vector_vIJK[IJK.axis.I],2)+pow(vector_vIJK[IJK.axis.J],2)) #length of projection of vector_vIJK to equatorial plane
        alpha=atan2(vector_vIJK[IJK.axis.J]/vepl,vector_vIJK[IJK.axis.I]/vepl)
    rdot=dot(vector_rIJK,vector_vIJK)/r
    alphadot=((vector_vIJK[IJK.axis.I]*vector_rIJK[IJK.axis.J])-(vector_vIJK[IJK.axis.J]*vector_rIJK[IJK.axis.I]))/(-pow(vector_rIJK[IJK.axis.J],2)-pow(vector_rIJK[IJK.axis.I],2))
    deltadot=(vector_vIJK[IJK.axis.K]-(rdot*(vector_rIJK[IJK.axis.K]/r)))/repl
    alpha=degrees(alpha)
    if alpha<0:
        alpha=360+alpha
    return r,alpha,degrees(delta),rdot,degrees(alphadot),degrees(deltadot)

def Sun(JDUT1):
    TUT1=(JDUT1-2451545.0)/36525
    lambdaMSun=NormalizeInRange((280.460+(36000.771*TUT1)),0,360) #must be normalized to 360 degrees; exact formula from Vallado
    TTDB=TUT1 #see Vallado, 5.1., p.279
    MSun=NormalizeInRange((357.5291092+(35999.05034*TTDB)),0,360) #must be normalized to 360 degrees
    lambdaecliptic=lambdaMSun+(1.914666471*sin(radians(MSun)))+(0.019994643*sin(2*radians(MSun)))
    rSun=1.000140612-(0.016708617*cos(radians(MSun)))-(0.000139589*cos(2*radians(MSun)))
    epsilon=23.439291-0.0130042*TTDB
    lambdaecliptic=radians(lambdaecliptic)
    epsilon=radians(epsilon)
    vector_rSun=dot(vector([rSun*cos(lambdaecliptic),rSun*cos(epsilon)*sin(lambdaecliptic),rSun*sin(epsilon)*sin(lambdaecliptic)]),AU)
    return vector_rSun

def Moon(JDTDB):
    TTDB=(JDTDB-2451545.0)/36525
    lambdaecliptic=NormalizeInRange((218.32+(481267.8813*TTDB)+MoonSinSeries(TTDB,[[6.29,134.9,477198.85],[-1.27,259.2,-413335.38],[0.66,235.7,890534.23],[0.21,269.9,954397.70],[-0.19,357.5,35999.05],[-0.11,186.6,966404.05]])),0,360) #must be normalized
    phiecliptic=MoonSinSeries(TTDB,[[5.13,93.3,483202.03],[0.28,228.2,960400.87],[-0.28,318.3,6003.18],[-0.17,217.6,407332.20]]) #returns not that value in degrees, which mentioned in the book. Don't know why, in "Methods of astrodynamics computer codes" there is same polinominal values
    P=0.9508+MoonCosSeries(TTDB,[[0.0518,134.9,477198.85],[0.0095,259.2,-413335.38],[0.0078,235.7,890534.23],[0.0028,269.9,954397.70]])
    epsilon=PowerSeries(TTDB,[23.439291,-0.0130042,-1.64e-7,5.04e-7])
    rMoon=Rearth/sin(radians(P)) #formula based on Vallado's Errata, p.2
    lambdaecliptic=radians(lambdaecliptic)
    phiecliptic=radians(phiecliptic)
    epsilon=radians(epsilon)
    vector_rMoon=dot(rMoon,vector([cos(phiecliptic)*cos(lambdaecliptic),(cos(epsilon)*cos(phiecliptic)*sin(lambdaecliptic))-(sin(epsilon)*sin(phiecliptic)),(sin(epsilon)*cos(phiecliptic)*sin(lambdaecliptic))+(cos(epsilon)*sin(phiecliptic))]))
    return vector_rMoon

def PlanetRV(Planet,JD): #planet name as string; returning R and V in km and km/s
    def HeliocentricElementsMEoD(planet,TTDB):
        fileName=planet+" MEoD.oe"
        coefficients_a,coefficients_e,coefficients_i,coefficients_Omega,coefficients__omega,coefficients_lambdaM=ReadOrbitalElementCoefficients(fileName)
        a=PowerSeries(TTDB,coefficients_a)
        e=PowerSeries(TTDB,coefficients_e)
        i=PowerSeries(TTDB,coefficients_i)
        Omega=PowerSeries(TTDB,coefficients_Omega)
        _omega=PowerSeries(TTDB,coefficients__omega)
        lambdaM=PowerSeries(TTDB,coefficients_lambdaM)
        return a,e,i,Omega,_omega,lambdaM
    yr,mo,day,h,min_,s=JDtoGregorianDate(JD)
    UTC=HMSToTime(h,min_,s)
    UT1,TAI,GPS,TT,TDB,TCB,TCG,TUT1,TTT,TTDB=ConvTime(yr,mo,day,UTC,-0.463326,32.0) #can be used directly, algorithm in book is incorrect as previous #37 UTC1toTAI
    a,e,i,Omega,_omega,lambdaM=HeliocentricElementsMEoD(Planet,TTDB)
    a=a*AU #converting to km, because we have mu in km^3/s^2
    M=lambdaM-_omega
    omega=_omega-Omega
    E=KepEqtnE(M,e)
    nu=NormalizeInRange(Anomalytonu(e, E, None, None, None, None),0,360) #must be normalized
    p=a*(1-pow(e,2))
    global mu
    currentmu=mu #saving current value of mu
    mu=muSunWiki() # We must switch mu for using Sun as central body.
    vector_rXYZ,vector_vXYZ=COE2RV(p,e,i,Omega,omega,nu,None,None,None)
    mu=currentmu #switching mu back to saved value
    epsilon=PowerSeries(TTT,[23.439279,-0.0130102,-5.086e-8,5.565e-7,1.6e-10,1.21e-11])
    vector_rXYZFK5=dot(ROT1(radians(-epsilon)),vector_rXYZ)
    vector_vXYZFK5=dot(ROT1(radians(-epsilon)),vector_vXYZ)
    return vector_rXYZFK5,vector_vXYZFK5 # vector from Sun. To calculate vector from Earth, subtract vector from Sun to Earth from result

def Site(Lat,Alt,LST): #Algorithm from Vallado's "Methods of astrodynamics - computer codes";
    Lat=radians(Lat)
    LST=radians(LST)
    x=abs((Rearth/(sqrt(1-(pow(eearth,2)*pow(sin(Lat),2)))))+Alt)*cos(Lat) #must be abs
    z=abs((Rearth*(1-pow(eearth,2))/(sqrt(1-(pow(eearth,2)*pow(sin(Lat),2)))))+Alt)*sin(Lat)
    vector_rIJK=vector([x*cos(LST),x*sin(LST),z])
    vector_vIJK=cross(vector([0.0,0.0,omegaearth]),vector_rIJK) #cross product; omegaearth is already converted to usage with time in seconds
    return vector_rIJK,vector_vIJK

def IJKtoLATLON(vector_r,thetaGMST): #Algorithm from Vallado's "Methods of astrodynamics - computer codes";
    #modified because we can not import LSTime from Vallado to avoid circular import
    r=sqrt(pow(vector_r[IJK.axis.I],2)+pow(vector_r[IJK.axis.J],2)+pow(vector_r[IJK.axis.K],2))
    alpha=degrees(atan(vector_r[IJK.axis.J]/vector_r[IJK.axis.I]))
    Long=alpha-thetaGMST
    delta=degrees(atan(vector_r[IJK.axis.K]/sqrt(pow(vector_r[IJK.axis.I],2)+pow(vector_r[IJK.axis.J],2))))
    Latgc=delta
    f=0.003352810664747352
    deltaLatPrev=0
    deltaLatCurr=0
    while True:
        Rc=Rearth*sqrt((1-((2*f)-pow(f,2)))/(1-(((2*f)-pow(f,2))*pow(cos(radians(Latgc)),2))))
        Latgd=degrees(atan((1/pow(1-f,2))*tan(radians(Latgc))))
        Height=sqrt(pow(r,2)-(pow(Rc,2)*pow(sin(radians(Latgd-Latgc)),2)))-(Rc*cos(radians(Latgd-Latgc)))
        deltaLatCurr=degrees(asin((Height/r)*sin(radians(Latgd-Latgc))))
        Latgc=delta-deltaLatCurr
        if deltaLatPrev-deltaLatCurr<0.00001:
            break
        else:
            deltaLatPrev=deltaLatCurr
    return Latgc,Latgd,Long,Height
