
import pandas as pd
import matplotlib.pyplot as plt
d = {'month_number': [1, 2, 3], 'facecream': [250, 300, 280], 'facewash': [150, 180, 160],
     'toothpaste': [400, 420, 410], 'bathingsoap': [300, 310, 305], 'shampoo': [200, 210, 205],
     'moisturizer': [100, 110, 105], 'total_units': [1400, 1530, 1465], 'total_profit': [7000, 7650, 7325]}
df = pd.DataFrame(d)
df.to_csv('sales.csv', index=False)
df = pd.read_csv('sales.csv')
plt.scatter(df['month_number'], df['toothpaste'])
plt.show()
df.plot(x='month_number', y=['facecream', 'facewash'], kind='bar')
plt.show()
tot = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
plt.pie(tot, labels=tot.index, autopct='%1.1f%%')
plt.show()
