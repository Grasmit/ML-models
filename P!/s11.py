import tensorflow as tf

''' Write a python function S(X) which takes an 2D TF tensor and returns the
softmax, applied row-wise, as a TF tensor. The function must work for tensors
X with an arbitrary number of rows! Print out results for ~x = [−1, −1, 5] and
~x = [1, 1, 2]! '''

def softMax(inp):
    e = tf.exp(inp)
    rowSum = tf.reduce_sum(e,axis=0)
    print(rowSum)
    return inp/rowSum

if __name__ == "__main__":
    x = [-1,-1,5]

    out = softMax(x)

    print("Out : ",out)