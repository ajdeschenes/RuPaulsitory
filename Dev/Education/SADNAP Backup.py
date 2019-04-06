### SADNAP Backup
# 10:29 pm, 4/5/2019
# Jupyter Notebook keeps returning error when attempting to save: '_xsrf argument missing from POST'

import pandas as pd

df = pd.DataFrame
df = pd.read_csv('~/Desktop/IL_report_cards_ISBE.net/rc07.csv',delimiter=',',dtype=str,header=None,low_memory=False)

df.head()

cities = pd.Series
cities = df[4]
cities.value_counts()

'''
contains_chicago = cities.str.contains('CHICAGO')
contains_chicago.value_counts()
# 39 more than we want

False    3248
True      640
Name: 4, dtype: int64
'''

matches_chicago = cities.str.match('CHICAGO')
matches_chicago.value_counts()
# 18 more than we want

'''
starts_chicago = cities.str.startswith('CHICAGO')
starts_chicago.value_counts()
# also 18 more than we want

False    3269
True      619
Name: 4, dtype: int64
'''

'''
ends_chicago = cities.str.endswith('CHICAGO')
ends_chicago.value_counts()
# WTF. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.endswith.html#pandas.Series.str.endswith

False    3888
Name: 4, dtype: int64
'''

'''
fake_chicagos = ['WEST CHICAGO','SOUTH CHICAGO HEIGHTS','NORTH CHICAGO','CHICAGO RIDGE','CHICAGO HEIGHTS'] # https://en.wikipedia.org/wiki/List_of_municipalities_in_Illinois
is_fake = cities.isin(fake_chicagos)
is_fake.value_counts()
# WTF. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin
'''

'''
is_fake = cities.isin(['WEST CHICAGO','SOUTH CHICAGO HEIGHTS','NORTH CHICAGO','CHICAGO RIDGE','CHICAGO HEIGHTS'])
is_fake.value_counts()
# WTF. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin

False    3888
Name: 4, dtype: int64
'''

# Forget it. Just take the 619 "matches."

# Add matches_chicago Series to DataFrame as new column
df['matches_chicago'] = matches_chicago
df.head()

df = df.loc[df['matches_chicago']==True]
df
'''
fake_chicagos = ['WEST CHICAGO',
 'SOUTH CHICAGO HEIGHTS',
 'NORTH CHICAGO',
 'CHICAGO RIDGE',
 'CHICAGO HEIGHTS']
'''

cities = df[4]
is_west = cities.str.contains('WEST') # False: 619
is_heights = cities.str.contains('HEIGHTS') # False 604, True 15
is_north = cities.str.contains('NORTH') # False: 619
is_ridge = cities.str.contains('RIDGE') # False 616, True 3

df['is_west'] = is_west
df['is_heights'] = is_heights
df['is_north'] = is_north
df['is_ridge'] = is_ridge

df = df.loc[df['is_west']==False]
df = df.loc[df['is_heights']==False]
df = df.loc[df['is_north']==False]
df = df.loc[df['is_ridge']==False]
len(df) # 601. HOT. DAMN.
print(df)



