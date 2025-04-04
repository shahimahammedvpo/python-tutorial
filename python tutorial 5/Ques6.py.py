

import pandas as pd
d = {'SN': [1, 2, 3], 'Name': ['Linus Torvalds', 'Tim Berners-Lee', 'Guido van Rossum'],
     'Country': ['Finland', 'England', 'Netherlands'],
     'Contribution': ['Linux Kernel', 'World Wide Web', 'Python'], 'Year': [1991, 1990, 1991]}
df = pd.DataFrame(d)
df.to_csv('contrib.csv', index=False)
print("Data written to contrib.csv")
