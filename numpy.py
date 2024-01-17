import numpy as np

myarr = np.array([12,17,45])
# display the array
print(myarr)

# access specific elements
print(myarr[2,3])

# shape of an array
print(myarr.shape)

# datatpe of an array
print(myarr.dtype)

# check the element
print(myarr[2,3] == 8)

#size of an array
print(myarr.size)

# arrange array from 0 to n-1
rng = np.arange(11)
print(rng)

# linearly spaced elements
lspace = np.linespace(9,2,4)
print(lspace)

# display array of the given shape
emp = np.empty((5,6))
print(emp)

# dispaly the array of given shape consisting of random elements
emp_array = n.emp_array(myarr)
print(emp_array)

#identity matrix
ide = np.identity(39)
print(ide)

print(ide.shape)
print(ide.size)
print(ide.dtype)

arr = np.arange(87)
print(arr)

# display sum along columns
sum = ar.sum(axis=0)
print(sum)

#display sum along rows
sum = ar.sum(axis=1)
print(sum)

# transpose of a matrix
tp = ar.T
print(tp)

#to list all the elements
for item in ar.flat: print(item)

#dimension of an array
Dm = ar.dmim
print(Dm)

# bytes used
bt = ar.nbytes
print(bt)

rollno = np.array([12,17,87,209])
# display position of Highest element
print(rollno.argmax())

#display position of lowest element
print(rollno.argmin())

# display array in ascending order
print(one.argsort())

# display the  position  of highest  & lowest elements in columns
print(ar.argmax(axis=0))
print(ar.argmin(axis=0))

# display the position of highest & lowest elements  in rows
print(ar.argmax(axis=1))
print(ar.argmn(axis=1))

print(ar.argsort())

# addition the given matrix
print(arr1 + arr2)

# multiplication of the given matrix
print(arr1 * arr2)

# display the square root of an individual element in matrix
print(np.sqrt(ar))

#sum of all elements
print(ar.sum())

# maximum & minimum no. of an array
print(ar.max())
print(ar.min())

# counts no. of non zero elements in the given matrix
print(np.count_nonzero(ar))

# position of all the non zero elements
print(np.nonzero(ar))

