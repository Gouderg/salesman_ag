import pandas as pd

name = "csv/berlin52.csv"

df = pd.read_csv(name, sep=",", header=None)
print(list(df[0]))
# del df[0]
# df.to_csv(name, sep=",", header=None, index=False)