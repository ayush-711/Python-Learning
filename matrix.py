from numpy import * 
arr = array([
    [1,2,3] ,
    [4,5,6]
])

print(arr) # to know about array data

print(arr.dtype) #to know what kind of data we're working with 

print(arr.size) #to know the total number of elements

print(arr.ndim) #to know the dimension of the array , here it is 2 , i.e it is 2D array

print(arr.shape) #it gives us the number of rows , column , here it is 2X3 , i.e 2 rows and 3 columns

arr2 = arr.flatten() #to form a new array with less dimension , i.e from 2D to 1D.
print(arr2)

m = matrix(arr)

print(min(m))

print(diagonal(m))

arr2 = array([
    [3,5] , [9,8] , [4,5]
])

m2 = matrix(arr2)

m3 = m + m2
print(m3)

m3 = m*m2
print(m3)
