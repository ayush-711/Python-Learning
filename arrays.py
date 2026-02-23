# How to copy content from a old Array into a New Array

from array import *

vals = array("i" , [2,3,5,18,9])

new_array = array(vals.typecode ,( a for a in vals))

for e in new_array:
    print(e)