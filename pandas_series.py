ser1 = {'col1':1,'col2':2,'col3':3}
ser2 = {'col1':4,'col2':5,'col3':6}

import pandas as pd

df = pd.concat([ser1,ser2])
print(df)