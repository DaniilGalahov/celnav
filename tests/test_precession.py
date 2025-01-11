import sys
sys.path.append("..\src")

import precession
import unittest

class test_precession(unittest.TestCase):
    def test_AnglesFor(self):
        Y=2028
        M=11
        D=13
        h=19
        m=0
        s=0
        zeta,z,theta=precession.AnglesFor(Y,M,D,h,m,s)
        self.assertAlmostEqual(zeta,0.1849341,4) #matching values from Meeus
        self.assertAlmostEqual(z,0.1849524,4)
        self.assertAlmostEqual(theta,0.1607080,4)

    def test_CorrectionFor(self):
        Y=2028
        M=11
        D=13
        h=19
        m=0
        s=0
        zeta,z,theta=precession.AnglesFor(Y,M,D,h,m,s)
        alpha0=41.054063
        delta0=49.227750
        alpha,delta=precession.CorrectionFor(alpha0,delta0,zeta,z,theta)
        self.assertAlmostEqual(alpha,41.547214,4)  #matching values from Meeus
        self.assertAlmostEqual(delta,49.348483,4)

    def test_RotationMatrixFrom(self):
        Y=2024
        M=12
        D=25
        h=14
        m=0
        s=0
        zeta,z,theta=precession.AnglesFor(Y,M,D,h,m,s)
        R=precession.RotationMatrixFrom(zeta,z,theta)
        self.assertAlmostEqual(R[0][0],9.99981446e-01,4) #provides correct precession
        self.assertAlmostEqual(R[0][1],-5.58704354e-03,4)
        self.assertAlmostEqual(R[0][2],-2.42750886e-03,4)
        self.assertAlmostEqual(R[1][0],5.58704354e-03,4)
        self.assertAlmostEqual(R[1][1],9.99984392e-01,4)
        self.assertAlmostEqual(R[1][2],-6.78165296e-06,4)
        self.assertAlmostEqual(R[2][0],2.42750886e-03,4)
        self.assertAlmostEqual(R[2][1],-6.78107056e-06,4)
        self.assertAlmostEqual(R[2][2],9.99997054e-01,4)

if __name__ == '__main__':
    unittest.main()
