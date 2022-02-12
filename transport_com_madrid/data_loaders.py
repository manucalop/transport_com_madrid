from abc import abstractmethod, ABC
import yaml
import pandas as pd
# Local imports
from .locations import ILocation
from .utils import xy2gps

class IStationsDataLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def get_nearby(self, location : ILocation, max_distance : float) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_station(self, idx : int = -1, name : str = '') -> pd.DataFrame:
        pass

class BicycleStationsDataLoader(IStationsDataLoader):
    def __init__(self):
        # Load data on creation
        with open('./config.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        self.filename = data['stations_files']['bicycle_stations']
        self.load_data()


    def load_data(self):
        self.data = pd.read_excel(self.filename)
        # Drop location missings
        self.data.dropna(subset=['latitude','longitude'], inplace=True)
        self.data.set_index('id', inplace=True, drop=False)

    def get_nearby(self, location : ILocation, max_distance : float) -> pd.DataFrame:
        df = self.data
        # Add distance column
        df['distance'] = df[['latitude','longitude']].apply(location.get_distance, axis='columns')
        # Filter out those exceeding maximum distance
        df = df[df['distance'] < max_distance]
        # Return ordered list
        return df.sort_values('distance')

    def get_station(self, idx : int = -1, name : str = '') -> pd.DataFrame:
        return self.data[(self.data['id'] == idx) |
                         (self.data['name'] == name)]

class BusStationsDataLoader(IStationsDataLoader):
    def __init__(self):
        # Load data on creation
        with open('./config.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        self.filename = data['stations_files']['bus_stations']
        self.load_data()

    def load_data(self):
        df = pd.read_csv('./data/buses_madrid.csv')
        #Drop missing location values
        df.dropna(subset=['X','Y'], inplace=True)
        #Get latitude and longitude columns
        df[['longitude','latitude']] = df[['X','Y']].apply(xy2gps, axis='columns')
        #Clean id column
        df['IDESTACION'] = pd.to_numeric(df['IDESTACION'].str[2:])
        #Set it as index
        df.set_index('IDESTACION', inplace=True, drop=False)
        #Save it
        self.data = df

    def get_nearby(self, location : ILocation, max_distance : float) -> pd.DataFrame:
        df = self.data
        # Add distance column
        df['distance'] = df[['latitude','longitude']].apply(location.get_distance, axis='columns')
        # Filter out those exceeding maximum distance
        df = df[df['distance'] < max_distance]
        # Return ordered list
        return df.sort_values('distance')

    def get_station(self, idx : int = -1, name : str = '') -> pd.DataFrame:
        return self.data[(self.data['IDESTACION'] == idx) |
                         (self.data['DENOMINACION'] == name)]
