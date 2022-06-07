import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRVAvF0t3qB6eaTRiwD-OIT2AAaFPHnJHQuZLhv2fNJ-_lCgwBkwYXYk4QJDCqig4dYsgPkS0v6Mk2Z/pub?gid=658228077&single=true&output=csv")
del df['full_name']
df = df.dropna()
df.to_csv(r'output.csv', index = False)
