import sys
sys.path.append("..\src")

from celestialobject import CelestialObject
import unittest

class test_celestialobject(unittest.TestCase):
    def test_init(self):
        Sun=CelestialObject("Sun")
        self.assertEqual(Sun.name,"Sun")
        self.assertEqual(Sun.type,"Sun")
        Moon=CelestialObject("Moon")
        self.assertEqual(Moon.name,"Moon")
        self.assertEqual(Moon.type,"Moon")
        Venus=CelestialObject("Venus")
        self.assertEqual(Venus.name,"Venus")
        self.assertEqual(Venus.type,"Planet")
        Deneb=CelestialObject("Deneb")
        self.assertEqual(Deneb.name,"Deneb")
        self.assertEqual(Deneb.type,"Star")
        

if __name__ == '__main__':
    unittest.main()
