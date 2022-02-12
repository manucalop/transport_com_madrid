import unittest
from transport_com_madrid.locations import GPSLocation

class TestLocations(unittest.TestCase):
    def test_gps_location(self):
        tolerance = 0.01 

        lat_1, lon_1 = 40, 40
        lat_2, lon_2 = 50, 50
        known_distance = 1358*1e3 # https://www.nhc.noaa.gov/gccalc.shtml

        loc1 = GPSLocation(lat_1, lon_1)
        loc2 = GPSLocation(lat_2, lon_2)
        d12 = loc1.get_distance(loc2.coordinates) # Meters to km

        absolute_error = abs(known_distance - d12)
        relative_error = absolute_error/max(known_distance,d12)

        self.assertLessEqual(relative_error,tolerance,'Wrong GPS Distance Calculation')

if __name__ == '__main__':
    unittest.main()

