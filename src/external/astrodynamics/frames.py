#frames representation, to avoid mistakes with numbers
class Axis:
    X=0
    Y=1
    Z=2

class Frame:
    def __init__(self):
    	self.axis=Axis()

class IJK(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.axis.I=self.axis.X
        self.axis.J=self.axis.Y
        self.axis.K=self.axis.Z
        #self.axis.DelXYZ()

XYZ=Frame()
IJK=IJK()
