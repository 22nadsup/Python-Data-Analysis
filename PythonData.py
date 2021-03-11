import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

passmark = 40

df = pd.read_csv("StudentsPerformance.csv")

df.head()

print (df.shape)

df.describe()

df.isnull().sum()

p = sns.countplot(x="math score", data = df, palette="muted")
_=plt.setp(p.get_xticklabels(), rotation=90)

df['Math_PassStatus'] = np.where(df['math score']<passmark, 'F', 'P')
df.Math_PassStatus.value_counts()

df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F', 'P')
df.Reading_PassStatus.value_counts()

df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
df.Writing_PassStatus.value_counts()

df['OverAll_PassStatus'] = df.apply(lambda x : 'F' if x['Math_PassStatus'] == 'F' or x['Reading_PassStatus'] == 'F' or x['Writing_PassStatus'] == 'F' else 'P', axis =1)
df.OverAll_PassStatus.value_counts()

df['Total_Marks'] = df['math score']+df['reading score']+df['writing score']

p = sns.countplot(x='gender', data = df, hue='OverAll_PassStatus', palette='bright')
p = sns.countplot(y='gender', data = df, hue='Total_Marks', palette='bright')
#_=plt.setp(p.get_xticklables(), rotation=90)

estimator=df.mean

print (df.mean)

plot_data = df['Total_Marks']
overall_score = df['Total_Marks']

overall_score = list(range((len(plot_data))))