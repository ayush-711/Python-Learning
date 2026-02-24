# i = 0
# def greet():
#     global i 
#     print("hello" , i)
#     i+=1
#     greet()

# greet()

#factorial using Recursion

def fact(n):

    if(n == 0):
        return 1
    n = n * fact(n-1)
    return n



n = int(input("enter the number : "))
factorial = fact(n)

print(factorial)