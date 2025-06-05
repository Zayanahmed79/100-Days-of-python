# Map 

# lst = [1, 2, 3, 4, 5, 4 , 8, 2]
# cube = lambda x : (x ** 3)

# newlist = list(map(lambda x : (x ** 3), lst))
# print(newlist)


# Filter

# def filterlist(a):
#     return a > 3

# newl = list(filter(lambda x : x > 2, lst))
# print(newl)

from functools import reduce

rlist = [1,2,3,4,5]

new_rlist = reduce(lambda x,t : x + t, rlist)
print(new_rlist)


