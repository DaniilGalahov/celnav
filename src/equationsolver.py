#simple equation solver
def LinEq22(a1,b1,h1,a2,b2,h2):
    d=(a1*b2)-(a2*b1)
    dx=(h1*b2)-(h2*b1)
    dy=(a1*h2)-(a2*h1)
    x=dx/d
    y=dy/d
    return x,y
