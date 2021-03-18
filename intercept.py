#simple celestial fix intercept algorithm
import astrometry as astro
from trigonometry import cos

observation = astro.Observation("Observation1.cfg")
print("p, nmi = "+str(round(observation.distance,2)))
print("Z, deg = "+str(round(observation.Z,2)))
