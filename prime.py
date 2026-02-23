# WAP to find if a number is prime or not.

import math as m

x = int(input("enter the number : "))

if x <= 1:
    print("not prime")

elif x == 2:
    print("prime number")


else:
    for i in range(2 , int(m.sqrt(x)) + 1):
        if x%i == 0 :
            print("not a prime")
            break
    else:
        print("prime number")
            