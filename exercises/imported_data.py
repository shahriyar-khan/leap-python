import pandas as pd
import urllib
from urllib.request import urlretrieve


url = 'http://winterolympicsmedals.com/medals.csv'
urlretrieve(url, 'medals.csv')
df_web = pd.read_csv('medals.csv')
print(df_web.shape)
df_web.head()