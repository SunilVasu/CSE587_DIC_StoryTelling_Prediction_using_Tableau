
import pandas as pd

df = pd.read_csv('crime.csv')


spike_cols = list({col for col in df['Month'] if '2017' in col})

print(spike_cols)
print(len(df))
res = df.loc[~df['Month'].isin(spike_cols)]

print(len(res))

res.to_csv('excluding2017crime.csv')

