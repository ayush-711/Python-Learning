av_candy = 4

ask = int(input("How many candies do you want? : "))
i = 1

while i <= ask:
    if i > av_candy :  
        print("out of stock")
        break

    print(i , "candy" )
    i = i + 1

