import numpy as np

''' Create a 1D array with entries from -100 to 0(included) in steps of 2 '''

a = np.arange(-100,1,2)

print("A : ",a)

print("------------------------------------------------------------------------------------------------")

''' Create a 2D with 3 rows and 2 columns, with row entries 1,1..., 2,2,..., 3,3,...'''

b = np.indices((3,2))[0]+1

print("B : ",b)




print("------------------------------------------------------------------------------------------------")

'''  Create a 2D with 3 rows and 2 columns that has the value -1 everywhere '''

c = np.full((3,2),-1)

print("C : ",c)

print("------------------------------------------------------------------------------------------------")

''' Create a 3D tensor with shape (5,4,3) with random normal entries, with
mean 0 and standard deviation 1. '''

d = np.random.normal(loc=0,scale=1,size=(5,4,3))

print("D : ",d)


print("------------------------------------------------------------------------------------------------")
