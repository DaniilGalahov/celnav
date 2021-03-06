#fix by two celestial objects
import navigation as nav
from trigonometry import sin, cos, tg, arcsin, arctg
import equationsolver as es

observation1 = nav.Observation("Observation1.cfg")
p1=observation1.p
Z1=observation1.Z

observation2 = nav.Observation("Observation2.cfg")
p2=observation2.p
Z2=observation2.Z

x,y=es.LinEq22(sin(Z1),cos(Z1),p1,sin(Z2),cos(Z2),p2)

B=Be+(y/60.0)
L=Le+(x/60.0/cos(B))

print(angle.ToLatitude(B))
print(angle.ToLongtitude(L))
