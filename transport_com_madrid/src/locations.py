from abc import ABC, abstractmethod

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

class CartesianLocation(CartesianCoordinates,Location):
    def __init__(self, x : float, y : float, z : float = 0):
        super().__init__(x,y,z)
    def get_distance(self, coordinates : CartesianCoordinates): # : FlatLocation
        return ((self.x - coordinates.x)**2 + 
                (self.y - coordinates.y)**2 +
                (self.z - coordinates.z)**2)**0.5

class GPSLocation(GPSCoordinates,Location):
    def __init__(self, lat : float, lon : float, height : float = 0):
        super().__init__(lat, lon, height)
    def get_distance(self, coordinates : GPSCoordinates): # : FlatLocation
        pass #TODO


