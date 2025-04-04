
import pandas as pd
df = pd.read_csv('auto.csv')
df.fillna(0, inplace=True)
df.to_csv('auto_clean.csv', index=False)
mx = df.loc[df['price'].idxmax()]['company']
print(f"Most expensive: {mx}")
toy = df[df['company'] == 'toyota']
print(toy)
cnt = df['company'].value_counts()
print(cnt)
hp = df.groupby('company')['price'].max()
print(hp)
am = df.groupby('company')['average-mileage'].mean()
print(am)
srt = df.sort_values('price')
print(srt)
