import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a=sns.load_dataset("flights")
sns.relplot(x="passengers", y="month", data=a)

a=sns.load_dataset("flights")
sns.relplot(x="passengers", y="month", hue="year", data=a)


b=sns.load_dataset("tips")
sns.relplot(x="time", y="tip", kind="line", data=b)

#Scatter plot
sns.catplot(x="day", y="total_bill", data=b)

#Violin plot
sns.catplot(x="day", y="total_bill", kind="violin", data=b)

#Boxen plot
sns.catplot(x="day", y="total_bill", kind="boxen", data=b)


from scipy import stats
#For univariate distributions
c=np.random.normal(loc=5, size=100, scale=2)
sns.distplot(c)
sns.displot(c)

#Bivariate distributions



#Multiple Graphs
a=sns.load_dataset("iris")
b=sns.FacetGrid(a, col="species")
b.map(plt.hist, "sepal_length")

#Pair Grid
a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)


#Adding some Aesthetics
sns.set(style="dark")
a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)

#for boxplot
sns.set(style="white", color_codes=True)
a=sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=a)

# boxplot
sns.set(style="white", color_codes=True)
a=sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=a)
sns.despine(offset=10, trim=True)

#colors
c=sns.color_palette()
sns.palplot(c)

























