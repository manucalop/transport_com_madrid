import pandas as pd
from abc import ABC
# Local imports
from .data_loaders import IStationsDataLoader, BicycleStationsDataLoader, BusStationsDataLoader
from .locations import ILocation

class User:
    def __init__(self, location : ILocation):
        self.location = location
        self.bicycle_stations = BicycleStationsDataLoader()
        self.bus_stations = BusStationsDataLoader()

    def get_bicycle_stations(self, max_distance : float):
        return self.bicycle_stations.get_nearby(self.location, max_distance)

    def get_bus_stations(self, max_distance : float):
        return self.bus_stations.get_nearby(self.location, max_distance)

class Vehicle(ABC):
    def __init__(self, location : ILocation, stations : IStationsDataLoader):
        self.location = location
        self.stations = stations
    def get_station(self, idx : int = -1, name : str = '') -> pd.DataFrame:
        return self.stations.get_station(idx,name)

class Bicycle(Vehicle):
    def __init__(self, location : ILocation):
        super().__init__(location, BicycleStationsDataLoader())

class Bus(Vehicle):
    def __init__(self, location : ILocation):
        super().__init__(location, BusStationsDataLoader())
