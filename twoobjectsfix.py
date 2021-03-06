#fix by two celestial objects
import navigation as nav
from trigonometry import sin, cos, tg, arcsin, arctg
import equationsolver as es
import angle

observation1 = nav.Observation("Observation1.cfg")
p1=observation1.p
Z1=observation1.Z

observation2 = nav.Observation("Observation2.cfg")
p2=observation2.p
Z2=observation2.Z

if not observation1.Be==observation2.Be and not observation1.Le==observation2.Le:
    print("Observations fixing different estimated points. Check .cfg files.")
    quit()

x,y=es.LinEq22(sin(Z1),cos(Z1),p1,sin(Z2),cos(Z2),p2)

B=observation1.Be+(y/60.0)
L=observation1.Le+(x/60.0/cos(B))

print(angle.ToLatitude(B))
print(angle.ToLongtitude(L))

