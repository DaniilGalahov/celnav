import sys
sys.path.append("..\src")

import catalog
import unittest

class test_catalog(unittest.TestCase):
    def test_LoadDataFromSourceFor(self):
        catalog.dataSource=0
        alpha,delta,mu_alpha,mu_delta=catalog.LoadDataFromSourceFor("Vega")
        self.assertAlmostEqual(alpha,279.23410832,6)
        catalog.dataSource=1
        alpha,delta,mu_alpha,mu_delta=catalog.LoadDataFromSourceFor("Vega")
        self.assertAlmostEqual(alpha,279.23473479,6)

    def test_CreateLocalCatalogIn(self):
        catalog.dataSource=0
        catalog.CreateLocalCatalog()
        file=open("Data\catalog.dat","r")
        data=file.read()
        file.close()
        self.assertTrue(data.startswith('{"Acamar": [44.5654818, -40.30473491, -53.53, 25.71],'))

    def test_LoadDataFor(self):
        catalog.dataSource=0
        alpha,delta,mu_alpha,mu_delta=catalog.LoadDataFor("Deneb")
        self.assertAlmostEqual(alpha,310.3579727,6)

if __name__ == '__main__':
    unittest.main()
