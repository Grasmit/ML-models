import numpy as np

'''Numpy basics and slicing'''

arr = np.indices((50,5,5))[0]

'''  Slice out the 1st sample into an array x and print it!  '''

a = arr[0]

print("A : ",a)

print("------------------------------------------------------------------------------------------------")

b = arr.copy()

b[10,:,-2:] = -1

print("B : ",b[10])

print("------------------------------------------------------------------------------------------------")

''' Print the mean pixel value in the 10th data sample '''

c = arr[10].mean()

print("C : ",c)

print("------------------------------------------------------------------------------------------------")

#d) Generate the following variations of the 10th sample and store them in a new variable z:
z  = arr[9]
    
# just keep every 3rd row
z[::3,:]
print("Keep every 3rd row",z)

# just keep every 3rd column
z[:,::3]
print("Keep every 3rd column",z)


# inverse all rows but not columns
z[::-1,:]
print("inverse all row not column",z)


# invert rows but not colums, just keeping every 2th rows
z[::-2,:]
print("Inverse row, not column, keeping every row",z)


print("------------------------------------------------------------------------------------------------")

''' Apply the in-place transform 1 + x '''
  
#e) Apply the in-place transform   for 1 + x

arr += 1

print("1+X transformation",arr)

# if 1 - x  => ans   td *= -1 ,   td += 1