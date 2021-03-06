#simple celestial fix intercept algorithm
import navigation as nav
from trigonometry import cos

observation = nav.Observation("Observation1.cfg")
print("p, nmi = "+str(round(observation.distance,2)))
print("Z, deg = "+str(round(observation.Z,2)))
