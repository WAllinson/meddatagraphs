import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')
df['overweight'] = 0
df['gluc'] = df['gluc'].replace(1,0)
df['gluc'] = df['gluc'].replace([2,3], 1)
df['cholesterol'] = df['cholesterol'].replace(1,0)
df['cholesterol'] = df['cholesterol'].replace([2,3],1)

df_cat = df.melt(id_vars=['cholesterol','gluc','smoke','alco','active','overweight'], var_name='cardio')
risks = df_cat[df_cat['cardio'] == 'cardio']
counts = risks.value_counts()
pd.wide_to_long(counts, 'cardio',  )
#df_cat = sns.catplot(data=risks, col='cardio')
#plt.savefig('test_plot.png')


