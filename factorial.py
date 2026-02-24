# 3! = 3*2*1 => 6

def factorialok(n):
    
    multi = 1
    for i in range(1,n+1):
        if n == 1 or n == 0:
            print("1")
            break
        multi = multi * i
    print(multi)

n = int(input("enter the value : "))

factorialok(n)