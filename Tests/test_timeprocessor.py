import sys
sys.path.append("..\src")

import timeprocessor
import unittest

class test_timeprocessor(unittest.TestCase):
    def test_APyTimeToYMDhms(self):
        Y,M,D,h,m,s=timeprocessor.APyTimeToYMDhms("2023-10-27 21:54:12.1385")
        self.assertEqual(Y,2023)
        self.assertEqual(M,10)
        self.assertEqual(D,27)
        self.assertEqual(h,21)
        self.assertEqual(m,54)
        self.assertAlmostEqual(s,12.139,6)

    def test_YMDhmsToAPyTime(self):
        aPyTimeString=timeprocessor.YMDhmsToAPyTime(2024,12,18,14,29,36.413635)
        self.assertEqual(aPyTimeString,"2024-12-18 14:29:36.414")

    def test_DateTimeToYMDhms(self):
        Y,M,D,h,m,s=timeprocessor.DateTimeToYMDhms("27.10.2023","21:54")
        self.assertEqual(Y,2023)
        self.assertEqual(M,10)
        self.assertEqual(D,27)
        self.assertEqual(h,21)
        self.assertEqual(m,54)
        self.assertAlmostEqual(s,0,6)

    def test_ToSeconds(self):
        seconds=timeprocessor.ToSeconds("00:10:10.2")
        self.assertAlmostEqual(seconds,610.2,0)
        seconds=timeprocessor.ToSeconds("00:10")
        self.assertAlmostEqual(seconds,600,0)
        seconds=timeprocessor.ToSeconds("01")
        self.assertAlmostEqual(seconds,3600,0)

    def test_ToString(self):
        string=timeprocessor.ToString(600)
        self.assertEqual(string,"00:10:00.000")
        string=timeprocessor.ToString(4200.2568)
        self.assertEqual(string,"01:10:00.257")

    def test_ExactTimeZone(self):
        timeZone=timeprocessor.ExactTimeZone("30*10.0'E")
        self.assertAlmostEqual(timeZone,2.011,3)

    def test_TimeZone(self):
        timeZone=timeprocessor.TimeZone("30*10.0'E")
        self.assertAlmostEqual(timeZone,2,0)

if __name__ == '__main__':
    unittest.main()
