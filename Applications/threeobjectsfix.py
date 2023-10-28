#fix by two celestial objects
import astrometry as astro
from trigonometry import sin, cos, tg, arcsin, arctg
import equationsolver as es
import angle

observation1 = astro.Observation("Observation1.cfg")
p1=observation1.p
Z1=observation1.Z

observation2 = astro.Observation("Observation2.cfg")
p2=observation2.p
Z2=observation2.Z

observation3 = astro.Observation("Observation3.cfg")
p3=observation3.p
Z3=observation3.Z

if not observation1.Be==observation2.Be==observation3.Be and not observation1.Le==observation2.Le==observation3.Le:
    print("Observations fixing different estimated points. Check .cfg files.")
    quit()

Be=observation1.Be
Le=observation1.Le

def Fix(p1, Z1, p2, Z2, Be, Le):
    x,y=es.LinEq22(sin(Z1),cos(Z1),p1,sin(Z2),cos(Z2),p2)
    B=Be+(y/60.0)
    L=Le+(x/60.0/cos(B))
    return [B,L]

B1,L1 = Fix(p1,Z1,p2,Z2,Be,Le)
B2,L2 = Fix(p2,Z2,p3,Z3,Be,Le)
B3,L3 = Fix(p3,Z3,p1,Z1,Be,Le)
    
B=(B1+B2+B3)/3.0
L=(L1+L2+L3)/3.0

print(angle.ToLatitude(B))
print(angle.ToLongtitude(L))

