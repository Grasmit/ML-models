import numpy as np

''' Reduction '''

arr = np.indices((50,5,5))[0]


''' a) Compute the pixel variance for pixel 0,0 over all samples '''

a = np.var(arr[:,0,0])

print("A: ",a)

print("------------------------------------------------------------------------------------------------")

''' b) Compute the pixel argmax for pixel 0,0 over all samples '''

b = np.argmax(arr[:,0,0])

print("B : ",b)
print("------------------------------------------------------------------------------------------------")

''' c) Compute the “standard deviation image” over all samples '''

c = np.std(arr,axis=0)

print("C : ",c)
print("------------------------------------------------------------------------------------------------")

''' compute the row wise mean over all samples'''

d = np.mean(arr,axis=0)

print("D : ",d)

print("------------------------------------------------------------------------------------------------")

''' Compute the column-wise mean over all samples '''

e = np.mean(arr,axis=1)

print("D : ",e.shape)

