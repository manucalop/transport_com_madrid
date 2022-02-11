import unittest
from transport_com_madrid.locations import CartesianLocation, GPSLocation

class TestLocations(unittest.TestCase):
    def test_cartesian_location(self):
        x_1, y_1, z_1 = -1.0, -2.0, -3.0
        x_2, y_2, z_2 = 1.0, 2.0, 3.0

        loc1 = CartesianLocation(x_1, y_1, z_1)
        loc2 = CartesianLocation(x_2, y_2, z_2)
        d = ((x_2 - x_1)**2 + (y_2 - y_1)**2 + (z_2 - z_1)**2)**0.5
        self.assertEqual(loc1.get_distance(loc2), d, 'Wrong Cartesian Distance Calculation')
    def test_gps_location(self):
        tolerance = 0.01 

        lat_1, lon_1, height_1 = 40, 40, 0
        lat_2, lon_2, height_2 = 50, 50, 0
        known_distance = 1358*1e3 # https://www.nhc.noaa.gov/gccalc.shtml

        loc1 = GPSLocation(lat_1, lon_1, height_1)
        loc2 = GPSLocation(lat_2, lon_2, height_2)
        d12 = loc1.get_distance(loc2) # Meters to km
        print(d12)
        absolute_error = abs(known_distance - d12)
        relative_error = absolute_error/max(known_distance,d12)

        self.assertLessEqual(relative_error,tolerance,'Wrong GPS Distance Calculation')

if __name__ == '__main__':
    unittest.main()

