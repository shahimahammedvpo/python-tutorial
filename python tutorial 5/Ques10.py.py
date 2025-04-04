
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

d = {'rollno': [1, 2, 3], 'name': ['Jack', 'John', 'Alex'], 'place': ['NY', 'LA', 'SF'], 'mark': [85, 90, 88]}
df = pd.DataFrame(d)
df.to_csv('stud.csv', index=False)
df = pd.read_csv('stud.csv')
print(df)
df.set_index('rollno', inplace=True)
print(df)
print(df[['name', 'mark']])
srt_nm = df.reset_index()[['rollno', 'name', 'mark']].sort_values('name')
print(srt_nm)
srt_mk = df.reset_index()[['rollno', 'name', 'mark']].sort_values('mark', ascending=False)
print(srt_mk)
avg = df['mark'].mean()
med = df['mark'].median()
mod = stats.mode(df['mark'])[0]
print(f"Avg: {avg}, Median: {med}, Mode: {mod}")
mn = df['mark'].min()
mx = df['mark'].max()
print(f"Min: {mn}, Max: {mx}")
var = df['mark'].var()
std = df['mark'].std()
print(f"Variance: {var}, Std Dev: {std}")
df['mark'].hist()
plt.show()
df.drop('place', axis=1, inplace=True)
print(df)
