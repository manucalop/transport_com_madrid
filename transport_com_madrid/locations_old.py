from abc import ABC, abstractmethod
from pyproj import Geod

class Coordinates(ABC):
    pass

class CartesianCoordinates(Coordinates):
    def __init__(self, x : float = 0, y : float = 0, z : float = 0):
        self.x = x
        self.y = y
        self.z = z

class GPSCoordinates(Coordinates):
    def __init__(self, lat : float = 0, lon : float = 0, height : float = 0):
        self.lat = lat
        self.lon = lon
        self.height = height

class Location(Coordinates):
    """
    Abstract location class. It enforces the creation of get_distance
    for a choice of coordinates.
    """
    @abstractmethod
    def get_distance(self, coordinates : Coordinates):
        pass
    @abstractmethod
    def set_coordinates(self, coordinates : Coordinates):
        pass

class CartesianLocation(CartesianCoordinates,Location):
    def __init__(self, x : float, y : float, z : float = 0):
        super().__init__(x,y,z)
    def get_distance(self, coordinates : CartesianCoordinates): # : FlatLocation
        return ((self.x - coordinates.x)**2 + 
                (self.y - coordinates.y)**2 +
                (self.z - coordinates.z)**2)**0.5
    def set_coordinates(self, coordinates : CartesianCoordinates):
        self.x = coordinates.x
        self.y = coordinates.y
        self.z = coordinates.z

class GPSLocation(GPSCoordinates,Location):
    def __init__(self, lat : float, lon : float, height : float = 0):
        super().__init__(lat, lon, height)
        self.geod = Geod(ellps="WGS84")
    def get_distance(self, coordinates : GPSCoordinates): # : FlatLocation
        return self.geod.line_length([self.lat, coordinates.lat],
                                     [self.lon, coordinates.lon])
    def set_coordinates(self, coordinates : GPSCoordinates):
        self.lat = coordinates.lat
        self.lon = coordinates.lon
        self.height = coordinates.height
