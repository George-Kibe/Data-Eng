import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

df=pd.read_csv("csvSamples/players_22.csv")
df.head(10)


#to delete a column
#del df['nation_flag_url']
df.head(20)

#horizontal countplot
plt.figure(figsize=(16,32))
sns.countplot(y=df.potential , palette="Set2")

#vertical countplot
plt.figure(figsize=(15,6))
sns.countplot(x="age", data=df)

