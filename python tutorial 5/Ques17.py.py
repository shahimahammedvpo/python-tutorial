

import pandas as pd
df = pd.read_csv('student.csv')
avg = df['CGPA'].mean()
print(f"Avg CGPA: {avg}")
high = df[df['CGPA'] > 9]
print(high)
cse_high = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print(cse_high)
mx = df.loc[df['CGPA'].idxmax()]
print(mx)
branch_avg = df.groupby('Branch')['CGPA'].mean()
print(branch_avg)
