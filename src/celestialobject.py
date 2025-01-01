from catalog import navigationStarNames

navigationPlanetNames=["Venus",
                       "Mars",
                       "Jupiter",
                       "Saturn"]

celestialObjectDiameters={"Sun":1392700.0,
                          "Moon":3474.2,
                          "Venus":12104.0,
                          "Mars":6779.0,
                          "Jupiter":139820.0,
                          "Saturn":116460.0}

Rearth=6378.137 #radius of Earth, km (from Vallado book)

class CelestialObject:
    def __init__(self, name): #name of celestial object must start from capital letter
        self.name=name        
        self.type=None        
        if self.name=="Sun":
            self.type="Sun"
        elif self.name=="Moon":
            self.type="Moon"
        elif self.name in navigationPlanetNames:
            self.type="Planet"
        elif self.name in navigationStarNames:
            self.type="Star"

    def VectorAt(self,Y,M,D,h,m,s):
        pass

    def GHAAt(self,Y,M,D,h,m,s):
        pass

    def DecAt(self,Y,M,D,h,m,s):
        pass

    def SHAAt(self,Y,M,D,h,m,s):
        pass

    def SDAt(self,Y,M,D,h,m,s):
        pass

    def HPAt(self,Y,M,D,h,m,s):
        pass
