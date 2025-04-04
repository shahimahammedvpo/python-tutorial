
import pandas as pd
d = {'x': [1, 2, 3], 'y': [4, 5, 6]}
df = pd.DataFrame(d)
df.to_excel('out.xlsx', index=False)
print("Data written to out.xlsx")

