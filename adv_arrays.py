from numpy import *

arr1 = array([1,2,6,4,5])
#arr2 = arr1.view() # FOR SHALLOW COPY

arr2 = arr1.copy() #FOR DEEP COPY

arr1[1] = 58

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))



