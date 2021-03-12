import pandas as pd 

d = {'Region': ['Southeast', 'Southwest', 'West', 'Midwest', 'Northeast', 'Pacific'],\
'Democrats':[6, 1, 8, 13, 14, 2],\
'Republicans':[20, 5, 10, 11, 7, 2],\
'Independents':[0, 0, 0, 0, 1, 0]
}
#print(d)
df = pd.DataFrame(data=d)
df.set_index('Region', inplace=True)
#print(df.head())
#give the conditional distribution of region for each political party
#totals
total_parties = df.sum()
print(total_parties)