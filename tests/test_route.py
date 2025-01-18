import sys
sys.path.append("..\src")

import route
import unittest

class test_route(unittest.TestCase):
    def test_DR(self):
        phi0=0
        lambda0=0
        V=110*1.852
        Vhdg=90
        D=10*1.852
        Dhdg=90
        dt=0.5
        phi1,lambda1=route.DR(phi0,lambda0,V,Vhdg,D,Dhdg,dt)
        self.assertAlmostEqual(phi1,0.0,6)
        self.assertAlmostEqual(lambda1,1.0,6)

if __name__ == '__main__':
    unittest.main()
