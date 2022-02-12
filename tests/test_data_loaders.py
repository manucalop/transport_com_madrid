import unittest
from transport_com_madrid.data_loaders import BicycleStationsDataLoader, BusStationsDataLoader
from transport_com_madrid.locations import GPSLocation

class TestBicycleStationsDataLoader(unittest.TestCase):
    def setUp(self):
        filename = './data/bicycles_madrid.xlsx'
        self.dl = BicycleStationsDataLoader(filename)

    def test_load_data(self):
        any_null_values = self.dl.data[['latitude', 'longitude']].isnull().values.any()
        self.assertEqual(any_null_values, False, 'Null values in latitude or longitude')
        self.assertEqual(len(self.dl.data) > 10, True, 'Not enough data entries')

    def test_get_nearby(self):
        df = self.dl.get_nearby(GPSLocation(lat=40.44030, lon=-3.695605), 1000)
        self.assertGreaterEqual(len(df), 0, 'Not finding nearby stations')

    def test_get_station(self):
        df = self.dl.get_station(idx = 153)
        self.assertGreaterEqual(len(df), 0, 'Not finding stations by index')
        df = self.dl.get_station(name = 'Alberto Alcocer')
        self.assertGreaterEqual(len(df), 0, 'Not finding stations by name')

class TestBusStationsDataLoader(unittest.TestCase):
    def setUp(self):
        filename = './data/buses_madrid.csv'
        self.dl = BusStationsDataLoader(filename)

    def test_load_data(self):
        any_null_values = self.dl.data[['latitude', 'longitude']].isnull().values.any()
        self.assertEqual(any_null_values, False, 'Null values in latitude or longitude')
        self.assertEqual(len(self.dl.data) > 10, True, 'Not enough data entries')

    def test_get_nearby(self):
        df = self.dl.get_nearby(GPSLocation(lat=40.44030, lon=-3.695605), 1000)
        self.assertGreaterEqual(len(df), 0, 'Not finding nearby stations')

    def test_get_station(self):
        df = self.dl.get_station(idx = 1514)
        self.assertGreaterEqual(len(df), 0, 'Not finding stations by index')
        df = self.dl.get_station(name = 'OFELIA NIETO-FRANCOS RODRIGUEZ')
        self.assertGreaterEqual(len(df), 0, 'Not finding stations by name')


if __name__ == '__main__':
    unittest.main()

