import pandas as pd
from collections import Counter

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRVAvF0t3qB6eaTRiwD-OIT2AAaFPHnJHQuZLhv2fNJ-_lCgwBkwYXYk4QJDCqig4dYsgPkS0v6Mk2Z/pub?gid=658228077&single=true&output=csv")
del df['full_name']
df = df.dropna()
df.to_csv(r'output.csv', index = False)


products = df["products"]
products = products.str.lower()
p = Counter(" ".join(products).split()).most_common(6)
rslt = pd.DataFrame(p, columns=['Product', 'Frequency'])
rslt2 = rslt.drop(rslt.index[0])

print("top 5 products bought:\n\n", rslt2)