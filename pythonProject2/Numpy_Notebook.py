import math

import numpy as np

print('why not?')

# to create a vector of zeros we use the np.zeros command
# we send the size in a list the column in the right and the
v = np.zeros([2, 4])
v = v + 2


# v[10][3] = 1001
# print(v)

# Multiplication should be done using np.dot(vector, vector) because it is incredibly faster than using a for

# to apply faster functions on each element of the array we can use functions in the imported library numpy

# np.log(vector) -> applies log on each element and returns a new vector
# print(np.log(v))

# np.abs(vector) -> applies abs on each element
# print(np.abs(v))

# to return a vector with each element to the power of m we use v**m
# print(v**3)

# to get the maximum we use np.max(vector)
# print(np.max(v))

# to apply 1/v to the vector we just write it like that
# print(1/v)

# if we want to reshape a vector we use reshape(size_y, size_x)
# print(v.reshape(100000, 1))

# we can also create a vector of e**v using np.exp(vector)
# print(np.exp(v))


# sigmoid function is very useful in machine learning
# here is an example of an easy type of function
def sigmoid(s):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    return 1 / (1 + np.exp(-s))


def sigmoid_diferential(x):
    return sigmoid(x) * (1 - sigmoid(x))


# to calculate the derivative of an array we have to apply the formula
# sigmoid(x) * (1 - sigmoid(x))
print(sigmoid_diferential(v))

# normalising is one of the most useful methods to converge faster
# as a reminder NORMALISATION of a matrix is
#           [1 , 2, 3]
# matrix =  [4, 5, 6]
#           [7, 8, 9]
# np.linalg.norm(matrix, ord = (order of the norm), axis = 1(rows), keepdims = true)
# print(np.linalg.norm(v, ord=3, axis=1, keepdims=True))


# Vectorisation
# x1 = np.ndarray([9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0])
# x2 = np.ndarray([9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0])
# print(str(np.ndarray.transpose(x1).shape[0]) + " " + str(x2.shape[0]))
# print(np.ndarray.transpose(x1))
# multiplies their elements
# x = np.dot(np.ndarray.transpose(x1), x2)







