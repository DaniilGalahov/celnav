#celestial fix by 2 intercepts (based on https://drive.google.com/file/d/0B6wCLzdYQE_gUF8zWDU0RG9uNm8/view)
import json
import angle
import navigation as nav
import timeprocessor
from trigonometry import sin, cos, tg, arcsin, arctg
import equationsolver as es

configFile=open("Celestial fix.cfg")
config = json.loads(configFile.read())

v=float(config["Ground speed"]) #ground speed, kts
HDG=angle.ToDecimal(config["Heading"]) #true heading

observation1 = nav.Observation("Observation1.cfg")
p1=observation1.p
Z1=observation1.Z

observation2 = nav.Observation("Observation2.cfg")
p2=observation2.p
Z2=observation2.Z

deltaTime=timeprocessor.SecondsToHours(observation2.time-observation1.time)
d=v*deltaTime #distance in nmi

p1=p1+(d*cos(HDG-Z1))

x,y=es.LinEq22(sin(Z1),cos(Z1),p1,sin(Z2),cos(Z2),p2)

B=Be+(y/60.0)
L=Le+(x/60.0/cos(B))

print(angle.ToLatitude(B))
print(angle.ToLongtitude(L))

