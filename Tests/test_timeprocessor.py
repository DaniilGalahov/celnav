import sys
sys.path.append("..")

import timeprocessor
import unittest

class test_timeprocessor(unittest.TestCase):
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

    def test_ToAstropyTimeString(self):
        apTimeString=timeprocessor.ToAstropyTimeString("27.10.2023","21:54")
        self.assertEqual(apTimeString,"2023-10-27 21:54")

    def test_HoursToSeconds(self):
        seconds=timeprocessor.HoursToSeconds(10)
        self.assertAlmostEqual(seconds,36000,0)

    def test_SecondsToHours(self):
        hours=timeprocessor.SecondsToHours(36000)
        self.assertAlmostEqual(hours,10,0)

    def test_ExactTimeZone(self):
        timeZone=timeprocessor.ExactTimeZone("30*10.0'E")
        self.assertAlmostEqual(timeZone,2.011,3)

    def test_TimeZone(self):
        timeZone=timeprocessor.TimeZone("30*10.0'E")
        self.assertAlmostEqual(timeZone,2,0)
        

if __name__ == '__main__':
    unittest.main()
