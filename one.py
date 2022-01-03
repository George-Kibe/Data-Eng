import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

mydata=pd.read_csv('csvSamples/zillow.csv')
mydata.head()
mydata.describe(include="all")
mydata.info()

#%matplotlib inline
histogram=mydata.hist(figsize=(5,10))
#histogram=plt.hist(mydata["Beds"])
#histogram.show()
pairplot=sns.pairplot(mydata)
#pairplot.show()

#getting the mean and standard deviation
mean=mydata['Beds'].mean()
print(mean)
stdev=mydata['Beds'].std()
print(stdev)

#create a linear regression model
regr=linear_model.LinearRegression()
y=mydata['']
x=mydata[[''], ['']]

regr.fit(x,y)
regr.coef_
regr.intercept_
