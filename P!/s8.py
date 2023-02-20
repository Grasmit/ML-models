import numpy as np
import matplotlib.pyplot as plt
import requests

import os


''' MNIST and matplotlib '''
def showAns(data):
  ''' Display samples nr. 5,6 and 7 in a single figure!  '''

  f,ax = plt.subplots(5,5)
  ax[0,0].imshow(data[5])
  ax[0,1].imshow(data[6])
  ax[1,0].imshow(data[7])

  print("------------------------------------------------------------------------------------------------")
  
  ''' Compute the mean pixel value for each image and display all means in a scatter plot!  '''
  meanVal = np.mean(data,axis=(1,2))

  total = data.shape[0]

  y = np.arange(0,total,1)

  print(meanVal.shape,y.shape)

  ax[2,0].scatter(y,meanVal)
  plt.xlim(0,60000)
  plt.ylim(0,256)

  print("------------------------------------------------------------------------------------------------")

  '''  Copy out all the images whose mean pixel value is > 0.3 and display 3 of them '''

  c = np.where((meanVal>0.3))
  c = data[c]

  ax[3,0].imshow(c[0])
  ax[3,1].imshow(c[1])
  ax[3,2].imshow(c[2])
 
  print("------------------------------------------------------------------------------------------------")
  
  ''' Compute the “variance image” over all samples and display it! '''

  varianceImage = np.var(data,axis=0)

  ax[4,0].imshow(varianceImage)


  plt.show()

def showlast2(data,label):
  '''  e) Copy out
    10 random images and display them in a single figure!  '''
  
  f,ax = plt.subplots(2,10)

  num = np.random.randint(0,60000,size=10)

  j = 0

  print(data[num[0]].shape)

  for i in num:
    ax[0,j].imshow(data[i])
    j+=1

  print("------------------------------------------------------------------------------------------------")  

  '''f) Copy out all samples of class 5 and display 10 of them'''

  label = np.argmax(label,axis=1)

  filter5 = np.where(label==5)

  print("this is filter",filter5[0])
  
  k = 0

  for i in filter5[0]:
    if k == 10:
      break
    ax[1,k].imshow(data[i])
    k+=1

  plt.show()

if __name__ == "__main__":
  
  ## read it into 'traind' and 'trainl'
  data = np.load("mnist.npz")
  traind = data["arr_0"] ;
  trainl = data["arr_2"] ;

  #showAns(traind)
  showlast2(traind,trainl)