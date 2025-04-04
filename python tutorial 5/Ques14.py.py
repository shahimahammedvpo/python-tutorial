

import pandas as pd
d = {'Reg_no': [10001, 10002, 10003], 'Name': ['Jack', 'John', 'Alex'],
     'Sub_Mark1': [76, 77, 74], 'Sub_Mark2': [88, 84, 79], 'Sub_Mark3': [76, 79, 81]}
df = pd.DataFrame(d)
df.to_csv('marks.csv', index=False)
print("Data written to marks.csv")
