import setup

import orthodromy
import unittest

class test_orthodromy(unittest.TestCase):
    def test_Between2Pos(self):
        phi1=59.7986813 #Pulkovo airport
        lambda1=30.2689333
        phi2=51.0257228 #Astana airport
        lambda2=71.4493939
        alpha1,alpha2,delta12,s12=orthodromy.Between2Pos(phi1,lambda1,phi2,lambda2)
        self.assertAlmostEqual(alpha1,92.4963366599314,6)
        self.assertAlmostEqual(alpha2,126.96312067753773,6)
        self.assertAlmostEqual(delta12,24.489647649865553,6)
        self.assertAlmostEqual(s12,2726.1751060897222,6) #difference with Google Maps about 3 km

    def test_PointHdg(self):
        phi1=59.7986813 #Pulkovo airport
        lambda1=30.2689333
        alpha1=92.4963366599314 #exact heading to Astana
        d=2726.1751060897222 #exact distance to Astana
        phi2,lambda2,alpha2=orthodromy.PointHdg(phi1,lambda1,alpha1,d)
        self.assertAlmostEqual(phi2,51.0257228,6)
        self.assertAlmostEqual(lambda2,71.4493939,6)
        self.assertAlmostEqual(alpha2,126.96312067753773,6)

if __name__ == '__main__':
    unittest.main()
