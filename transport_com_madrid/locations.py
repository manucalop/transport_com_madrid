from abc import ABC, abstractmethod
from pyproj import Geod

class ILocation(ABC):
    @abstractmethod
    def get_distance(self, coordinates : tuple) -> float:
        pass

    @abstractmethod
    def set_coordinates(self, coordinates : tuple) -> None:
        pass

class GPSLocation(ILocation):
    def __init__(self, lat : float, lon : float):
        self.lat = lat
        self.lon = lon
        self.geod = Geod(ellps="WGS84")

    def get_distance(self, coordinates : tuple) -> float:
        return self.geod.line_length([self.lat, coordinates[0]],
                                     [self.lon, coordinates[1]])

    def set_coordinates(self, coordinates : tuple) -> None:
        self.lat = coordinates[0]
        self.lon = coordinates[1]
