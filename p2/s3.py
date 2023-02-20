import numpy as np


a1 = np.random.randint(0,4,20)
a2 = np.random.randint(0,4,20)
print(a1)
print(a2)

confusion_matrix = np.zeros((4,4), dtype= int)
np.add.at(confusion_matrix, (a1,a2), 1)

print(confusion_matrix)

print("------------------------------------------------------------------------------------------------")

'''  Give a code snippet that generates two 1D arrays with values from 0 to 19
(included) in ascending order. Then, the code should shuffle both arrays such
that same positions contain same values after shuffling (like you would shuffle
train data and labels) '''

b1 = np.arange(0,20,1)
b2 = np.arange(0,20,1)

print(b1[:5],b2[:5])

random = np.random.randint(0,20,20)

b1 = b1[random]
b2 = b2[random]

print(b1[:5],b2[:5])

print("------------------------------------------------------------------------------------------------")

'''  Give a code snippet that creates a 1D array with random values from 0 to
9 (included). Then, interpret this array as scalar targets and create a one-hot
representation for them, assuming 10 classes. '''

c1 = np.random.randint(0,10,1)
c1 = c1[0]

print(c1)

oneHot = np.zeros((1,10))
print("before--",oneHot)

oneHot[0][c1] = 1
print("after--",oneHot)






