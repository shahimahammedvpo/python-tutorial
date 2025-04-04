
import pandas as pd

lst = [['A', 10], ['B', 20], ['C', 30]]
df = pd.DataFrame(lst, columns=['n', 'v'])
df.set_index('n', inplace=True)
print(df)
