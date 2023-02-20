import numpy as np

''' Broadcasting '''

arr = np.indices((50,5,5))[0]

''' create a 5-element row vector with entries from 1 to 5, and subtract it from
all rows of all samples using broadcasting '''

rowMat = np.arange(1,6,1)

a = arr - rowMat

print("A : ",a)

print("------------------------------------------------------------------------------------------------")

colMat = np.arange(1,6,1)
colMat = colMat.reshape(-1,1)

b = arr*colMat

print("B : ",b)

print("------------------------------------------------------------------------------------------------")

meanVal = np.mean(arr,axis=0)

c = arr - meanVal

print("C : ",c)