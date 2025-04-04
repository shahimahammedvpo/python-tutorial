
import pandas as pd
df = pd.read_csv('employee.csv')
print(df.head(7))
print(df['name'].sort_values())
mx = df.loc[df['salary'].idxmax()]['name']
print(f"Highest salary: {mx}")
males = df[df['gender'] == 'Male']['name']
print(males)
teams = df['team'].unique()
print(teams)
