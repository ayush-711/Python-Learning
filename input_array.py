# How to take input in array

from array import * 

arr = array("i" , [])

num = int(input("enter the length of array "))

for i in range(num):
    x = int(input("enter the next value "))
    arr.append(x)

print(arr)


ask = int(input("Enter the number you want to search! : "))

k = 0

for e in arr:
    if e == ask:
        print(k)
    k = k+1
