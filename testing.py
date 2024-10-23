import pandas as pd

df = pd.read_csv('medical_examination.csv')
df['Overweight'] = 0
df['gluc'] = df['gluc'].replace(1,0)
df['gluc'] = df['gluc'].replace([2,3], 1)
print(df['gluc'])


