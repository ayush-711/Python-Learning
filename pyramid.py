# #    *
# #   ***
# #  *****
# # *******
rows = 1
def pyramid(n):
    global rows
    # global space
    # global star
    
    space = " "
    star = "*"

    if(n > rows ):
       

        print(space*(n-rows) + star*(2*rows - 1) + space*(n-rows))
        rows = rows + 1
        # print(rows)
        pyramid(n)




n = int(input("enter number of rows "))
pyramid(n)




