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


























