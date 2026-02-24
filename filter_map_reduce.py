from functools import reduce


lst = [1,2,3,4,5,6,7,8,9,20]

evens = list(filter(lambda n : n%2 == 0 , lst))
print(evens)

triples = list(map(lambda n:n*3, evens))
print(triples)

sum = reduce(lambda a,b : a+b , evens)
print(sum)