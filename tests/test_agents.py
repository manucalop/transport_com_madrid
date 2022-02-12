import unittest
from transport_com_madrid.agents import User, Bicycle, Bus
from transport_com_madrid.locations import GPSLocation

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(GPSLocation(lat=40.45,lon=-3.71))
    def test_get_bicycle_stations(self):
        self.assertGreater(len(self.user.get_bicycle_stations(1000)),0,
                          'Empty bicycle stations nearby')
    def test_get_bus_stations(self):
        self.assertGreater(len(self.user.get_bus_stations(1000)),0,
                           'Empty bus stations nearby')

class TestBicycle(unittest.TestCase):
    def setUp(self):
        self.user = Bicycle(GPSLocation(lat=40.45,lon=-3.71))
    def test_get_bicycle_stations(self):
        self.assertGreater(len(self.user.get_station(idx=153)),0,
                          'Not finding stations by idx')
        self.assertGreater(len(self.user.get_station(name = 'Alberto Alcocer')),0,
                          'Not finding stations by name')

class TestBus(unittest.TestCase):
    def setUp(self):
        self.user = Bus(GPSLocation(lat=40.45,lon=-3.71))
    def test_get_bicycle_stations(self):
        self.assertGreater(len(self.user.get_station(idx=1514)),0,
                          'Not finding stations by idx')
        self.assertGreater(len(self.user.get_station(name = 'OFELIA NIETO-FRANCOS RODRIGUEZ')),0,
                          'Not finding stations by name')

if __name__ == '__main__':
    unittest.main()

