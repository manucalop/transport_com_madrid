from abc import ABC, abstractmethod
from pyproj import Geod

class ILocation(ABC):
    @abstractmethod
    def get_distance(self, coordinates : tuple) -> float:
        pass

class GPSLocation(ILocation):
    def __init__(self, lat : float, lon : float):
        self.coordinates = (lat, lon)
        self.geod = Geod(ellps="WGS84")

    def get_distance(self, coordinates : tuple) -> float:
        return self.geod.line_length([self.coordinates[0], coordinates[0]],
                                     [self.coordinates[1], coordinates[1]])
