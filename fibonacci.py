# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 ......

def fibo(n):
    a = 0 
    b = 1
    c = a + b

    print(a , end = " ")
    print(b , end = " ")

    for i in range(2 ,n):
        
        print(c , end = " ")

        a = b
        b = c
        c = a+b


n = int(input("enter the value of fibonacci series "))

fibo(n)