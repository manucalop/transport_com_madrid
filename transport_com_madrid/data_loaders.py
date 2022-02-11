from abc import abstractmethod
from locations import GPSLocation
import pandas as pd

class DataLoader:
    @abstractmethod
    def get_df(self) -> pd.DataFrame:
        pass

class BicycleDataLoader(DataLoader):
    def __init__(self, filename : str):
        self.filename = filename
    def get_df(self) -> pd.DataFrame:
        return pd.read_excel('./../data/2018_Julio_Bases_Bicimad_EMT.xlsx')


class User(GPSLocation):
    def __init__(self, lat : float, lon : float):
        super().__init__(lat, lon)
    def get_bicycle_stations(self, max_distance : float):
        # Query data
        df = pd.read_excel('./../data/2018_Julio_Bases_Bicimad_EMT.xlsx')
        # Drop any location missing
        df = df.dropna(subset=['latitude','longitude'])
        # Get distance
        df['distance'] = df[['latitude','longitude']].apply(self.get_distance, axis='columns')
        # Filter out those exceeding maximum distance
        df = df[df['distance'] < max_distance]
        # Return ordered list
        return df.sort_values('distance')


class Station(GPSLocation):
    def __init__(self, lat : float, lon : float, idx : int, name : str):
        super().__init__(lat, lon)
        self.idx = idx
        self.name = name

class Vehicle(GPSLocation):
    def __init__(self, lat : float, lon : float):
        super().__init__(lat, lon)

class Bicycle(Vehicle):
    def __init__(self, lat : float, lon : float):
        super().__init__(lat, lon)

# df = pd.read_excel('./../data/2018_Julio_Bases_Bicimad_EMT.xlsx')
# print(df.head())
# print(df.columns)
user = User(lat=40.44, lon=-3.69)
print(user.get_bicycle_stations(100000000000000000000))

#func = lambda x : x['latitude'] + x['longitude']

#df = pd.read_excel('./../data/2018_Julio_Bases_Bicimad_EMT.xlsx')
##Transform data
#df['distance'] = df[['latitude','longitude']].apply(func, axis='columns')
#df = df.sort_values('distance')
#print(df)
