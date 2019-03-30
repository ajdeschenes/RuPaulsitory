#%%
import pandas as pd

#%%
csv1 = pd.read_csv('Resources/Chicago Neighborhoods by Zipcode.csv', delimiter=',')
csv2 = pd.read_csv('Resources/UIC_gentrification_index_neighborhood_list.csv', delimiter=',')

csv2.merge(csv1, on='Neighborhood')
csv2.head()



#%%
csv1

#%%
