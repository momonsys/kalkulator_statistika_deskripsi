import pandas as pd

#input data
arr = input("masukan array:")
arr = list(map(float, arr.split(',')))
df = pd.DataFrame(arr)

#hasil bray
print(df.describe())
print("Modus   :",df.mode(numeric_only=True))
