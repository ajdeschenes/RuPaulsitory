
#%%
import pandas as pd
from pprint import pprint


#%%
csvfile = pd.read_csv('Resources/zips_and_hoods_from_chicagorealestatelocal.com.csv', header=None, delimiter=',')
print(str(csvfile.iloc[1]))
df = pd.DataFrame(csvfile)
print(df)


#%%
strings = []
zips = []
for string in df.iloc[:,0]:
    strings.append(string.split(' '))
pprint(strings)
df2 = pd.DataFrame(strings)
print(df2.head())
zips = df2.iloc[:,0]
print()
print(zips)


#%%



#%%



