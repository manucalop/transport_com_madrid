import pandas as pd
import pyproj 

proj = pyproj.Transformer.from_crs(32230, 4326, always_xy=True)
xy2gps = lambda x : pd.Series(proj.transform(x[0],x[1]))
