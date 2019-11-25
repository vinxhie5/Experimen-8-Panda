import pandas as pd

df = pd.read_csv('cars.csv')

b = df[0:5]
c = df[27:32]
print (b,c)