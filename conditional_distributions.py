#recreate khan problem from unit distributions
#and explain solution
import pandas as pd 

d = {'Region': ['Southeast', 'Southwest', 'West', 'Midwest', 'Northeast', 'Pacific'],\
'Democrats':[6, 1, 8, 13, 14, 2],\
'Republicans':[20, 5, 10, 11, 7, 2],\
'Independents':[0, 0, 0, 0, 1, 0]
}
#print(d)
df = pd.DataFrame(data=d)
df.set_index('Region', inplace=True)
df.head()
total_parties = df.sum()
total_parties
total_regions = df.sum(axis=1)
total_regions
type(total_regions)
type(total_parties)
total_parties.sum() == total_regions.sum()
total = total_regions.sum()
total
df["Regional_Prob"] = total_regions/total
df.head()
party_prob = total_parties/100
party_prob.rename("party_prob", inplace=True)
df = df.append(party_prob)
df