

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('weather.csv')
print(df.head(10))
mx = df['temperature'].max()
mn = df['temperature'].min()
print(f"Max Temp: {mx}, Min Temp: {mn}")
low = df[df['temperature'] < 28]['place']
print(low)
cloudy = df[df['weather'] == 'Cloudy']['place']
print(cloudy)
freq = df['weather'].value_counts()
print(freq)
df.plot(x='date', y='temperature', kind='bar')
plt.show()
