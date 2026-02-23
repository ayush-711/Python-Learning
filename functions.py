def greet():
    print("hello")
    print("how are you?")

greet()

def add(x,y):
    print(x+y)

add(6,8)


def add_sub_multi(x,y,z):
    add = x+y+z
    sub = x-y-x
    multi = (x*y*z)

    return add ,sub , multi

print(add_sub_multi(5 , 6 , 7))

result1 , result2 , result3 = add_sub_multi(5,6,7)

print(result1 , result2 , result3)
