import setup

import nutation
import angle
import unittest

class test_nutation(unittest.TestCase):
    def test_AnglesFor(self):
        Y=1987
        M=4
        D=10
        h=0
        m=0
        s=0
        deltaPsi,deltaEpsilon,epsilon=nutation.AnglesFor(Y,M,D,h,m,s)
        self.assertAlmostEqual(deltaPsi,-0.001073010699826682,6) #matching values from Meeus
        self.assertAlmostEqual(deltaEpsilon,0.00263000121548375,6)
        self.assertAlmostEqual(epsilon,23.440946387200604,6)
        
    def test_CorrectionFor(self):
        Y=2028
        M=11
        D=13
        h=19
        m=0
        s=0
        deltaPsi,deltaEpsilon,epsilon=nutation.AnglesFor(Y,M,D,h,m,s)
        alpha0=41.054063
        delta0=49.227750
        alpha,delta=nutation.CorrectionFor(alpha0,delta0,deltaPsi,deltaEpsilon,epsilon)
        self.assertAlmostEqual(alpha,41.05850294728335,6) #no reference values to check, so just hope that results looks logical
        self.assertAlmostEqual(delta,49.22845144382492,6)

if __name__ == '__main__':
    unittest.main()
