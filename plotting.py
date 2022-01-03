#importing matplotlib module
from matplotlib import pyplot as plt

###------------------------------------ LINE PLOTTING-------------------------------- ###
# x-axis values
#[x1,x2,x3,x4]
x=[5,2,9,4,7,10,12,20,8,14]

# y-axis values
#[y1,y2,y3,y4]
y=[10,5,8,4,2,8,11,15,12,16]

#Function to plot
plt.plot(x,y)

#function to show the plot
plt.show()

###----------------------------------BAR PLOTTING----------------------------------- ###
# x-axis values
#[x1,x2,x3,x4]
x= [5,2,9,4,7,10,12,20,8,14]

# y-axis values
#[y1,y2,y3,y4]
y= [10,5,8,4,2,8,11,15,12,16]

#Function to plot
plt.bar(x,y)

#function to show the plot
plt.show()

### --------------------------------HISTOGRAM PLOTTING------------------------------- ###
y=[13,1,2,6,4,15,25,9,6,5,12]
plt.hist(y)
plt.show()

### --------------------------------SCATTER PLOTTING-----------------------------------###
plt.plot([1,2,3,4,5,6,7,8,9,10], [1,4,9,16,25,36,49,64,81,100], 'ro')
#ro to make red circles
plt.axis([0,11,0,120])
plt.show()
