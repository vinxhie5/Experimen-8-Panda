import pandas as pd

df = pd.read_csv('cars.csv')

a = df.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]
print (a)

b = df.loc[0]
print (b)

c = df.loc[[23],['Model','cyl']]
print (c)

d = df.loc[[1,28,18],['Model','cyl','gear']]
print (d)