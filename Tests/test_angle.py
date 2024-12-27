import sys
sys.path.append("..\src")

import angle
import unittest

class test_angle(unittest.TestCase):
    def test_ToDecimal(self):
        self.assertAlmostEqual(angle.ToDecimal("245*40.0'"),245.666667,6)
        self.assertAlmostEqual(angle.ToDecimal("245*40.0' E"),245.666667,6)
        self.assertAlmostEqual(angle.ToDecimal("245*40.0' W"),-245.666667,6)

    def test_Normalize(self):
        self.assertAlmostEqual(angle.Normalize(250),250.0,6)
        self.assertAlmostEqual(angle.Normalize(370),10.0,6)
        self.assertAlmostEqual(angle.Normalize(-20),340.0,6)
        self.assertAlmostEqual(angle.Normalize(-179.75),180.25,6)
        self.assertAlmostEqual(angle.Normalize(-180.25),179.75,6)

    def test_ToSigned180(self):
        self.assertAlmostEqual(angle.ToSigned180(50),50,6)
        self.assertAlmostEqual(angle.ToSigned180(270),-90,6)
        self.assertAlmostEqual(angle.ToSigned180(-50),-50,6)

    def test_ToString(self):
        self.assertEqual(angle.ToString(250.5),"250°30.0'")
        self.assertEqual(angle.ToString(-19.5),"340°30.0'")

    def test_ToJSONCompatible(self):
        self.assertEqual(angle.ToJSONCompatible("250°30.0'"),"250*30.0'")

    def test_ToLatitude(self):
        self.assertEqual(angle.ToLatitude(50.5),"50°30.0' N")
        self.assertEqual(angle.ToLatitude(-10.5),"10°30.0' S")
        self.assertEqual(angle.ToLatitude(100.5),"79°30.0' N")
        self.assertEqual(angle.ToLatitude(-100.5),"79°30.0' S")

    def test_ToLongtitude(self):
        self.assertEqual(angle.ToLongtitude(50.5),"50°30.0' E")
        self.assertEqual(angle.ToLongtitude(-10.5),"10°30.0' W")
        self.assertEqual(angle.ToLongtitude(270.5),"89°30.0' W")
        self.assertEqual(angle.ToLongtitude(-270.5),"89°30.0' E")

if __name__ == '__main__':
    unittest.main()
