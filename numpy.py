
import numpy as np


Ar = np.array([12,34,4])                            # Display given array
print(Ar)


print(Ar.dtype)                                    # Datatype of an array


print(Ar.size)                                    # size of an array


A = np.array((23,45,36))
print(A)


print(Ar.ravel())                                 # reshape an array into 1D ARRAY


rng = np.arange(22)                              # arange attribute 
print(rng)


B = np.linspace(9,10,5)                         # linespace attribute
print(B)


zeros = np.zeros((8,9))                          # create an array of zeros of given shape 
print(zeros)


print(zeros.shape)                               # shape of an array 

print(zeros.size)                              # size of an array


emp_arr = np.empty((9,7))                      # an array of random elements
print(emp_arr) 


ide_arr = np.identity(11)                             # identity matrix
print(ide_arr)

print(ide_arr.shape)

print(ide_arr.size)

print(ide_arr.dtype)

Array = np.arange(78)
print(Array)

XYZ = [[12,3,4],[2,56,89],[9,9,3]]                               # multdimension array
arr = np.array(XYZ)
print(arr)

sum = arr.sum(axis=0)                                            # sum along columns
print(sum)

sum = arr.sum(axis=1)                                           # sum along rows
print(sum)

TP = arr.T                                                     # transpose of an array
print(TP)

for item in arr.flat:print(item)
Dim = arr.ndim                                                  # dimensions 
print(Dim)

BS = arr.nbytes                                               # overall bytes consumed
print(BS)

SEQ = np.array([23,67,90,45])                                # position of largest element         
print(SEQ.argmax())

print(SEQ.argmin())                                          # position of smallest element


print(SEQ.argsort())                                       # sort the element in ascending order


AB= ([12,34,67],[34,60,23])                                # addition of given matrices
BC = ([23,45,1],[65,32,34])     
print(AB + BC)

print(np.sqrt(arr))                                         # square root of individual elements in an array

print(np.count_nonzero(arr))                                 # counts non-zero elements 

print(np.nonzero(arr))                                        # positions of non-zero elements

