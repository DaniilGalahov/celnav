import sys
sys.path.append("..\src")

from external.math import *

import frame
import unittest

class test_frame(unittest.TestCase):
    def test_IJK2SEZ(self):
        vector_rIJK=vector([6378.137,0,0])
        phi=45.0
        thetaLST=90.0
        vector_rSEZ=frame.IJK2SEZ(vector_rIJK,phi,thetaLST)
        self.assertAlmostEqual(vector_rSEZ[0],0,6)
        self.assertAlmostEqual(vector_rSEZ[1],-6378.137,6)
        self.assertAlmostEqual(vector_rSEZ[2],0,6)
        

if __name__ == '__main__':
    unittest.main()
