import numpy as np

Array = np.array([1,2,3,4,5])           # Using list
print(Array)
print(type(Array))

Ar = np.array((1,2,3,4,5))              # Using Tuple
print(Ar)

Arr = np.arange(1,11)                   # Using Arange attribute
print(Arr)

A = np.linspace(1,20,8)                #  By linspace attribute
print(A)


B = np.zeros([3,4])                      #  Array gets filled with zeros
print(B)

Array = np.array([[1,2,3,4],[5,6,7,8]])
print(Array)
print(type(Array))

# Accessing the values

A = np.array([1,2,3,4])
print(A[0])
print()
print(A[3])

B = np.array([[1,23,12,234],[34,56,45,67]])
print(B[0][2])

# Changing the values

C = np.array(['A','B','C','D'])
C[1] = 'E'
print(C)

# Using the functions
D = np.array([1,2,3,4,5])

print(D.tolist())                # converting array into list
print()

print(D.size)                    # IT gives the size of the array
print()

print(D.nbytes)                  # Gives number of bytes
print()

print(D.argmax())                # gives the index position of the maximum value
print()

print(D.argmin())                # gives the index position of the minimum value
print()

print(D.argsort())               # arranges the index positions of an array in the ascending order of its elements
print()

