import numpy as np
import matplotlib.pyplot as plt

''' Matplot Lib. '''

''' a) plot the function 1/x between 1 and 5 using 100 support points!  '''

f,ax = plt.subplots(2,3)

x = np.linspace(1,5,100)

y = 1/x

ax[0,0].plot(x,y)

print("------------------------------------------------------------------------------------------------")

''' b) generate a scatter plot of the same data as in a)!  '''

ax[0,1].scatter(x,y)

print("------------------------------------------------------------------------------------------------")

''' c) generate a bar plot of the same data as in a)! '''

ax[0,2].bar(x,y)

print("------------------------------------------------------------------------------------------------")

''' d) plot 1/x and √x  together in a single plot, same range as before '''

ax[1,0].plot(x,y)
ax[1,0].plot(x,np.sqrt(x))

print("------------------------------------------------------------------------------------------------")

''' e) generate 100 numbers distributed according to a uniform distribution between 0 and 1, and display their histogram!'''

data = np.random.uniform(0,1,100)

ax[1,1].hist(data,bins=10)

plt.show()

