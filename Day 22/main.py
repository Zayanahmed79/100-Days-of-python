l = [1, 4, 7, 9, 12]
print(l[0])  # 1
print(l[1])  # 4    
print(l[2])  # 7


# negative indexing
print(l[-1])  # 12
print(l[-2])  # 9   
print(l[-3])  # 7
print(l[-4])  # 4
print(l[-5])  # 1


# Slicing
print(l[0:3])  # [1, 4, 7]
print(l[1:4])  # [4, 7, 9]
print(l[2:])   # [7, 9, 12]

print(l[:3])   # [1, 4, 7]
print(l[1:])   # [4, 7, 9, 12]

# Slicing with negative indices
print(l[-3:-1])  # [7, 9] , as [-1] is excluded b/c of slicing rules
print(l[-4:])    # [4, 7, 9, 12]

# Slicing with step
print(l[::2])  # [1, 7, 12] , every second element  
print(l[1::2])  # [4, 9] , starting from index 1, every second element
print(l[::-1])  # [12, 9, 7, 4, 1] , reversed list 


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

# List comprehensions
list = [i for i in range(1, 11) ]
print(list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List comprehensions with calculations
list = [i*i for i in range(1, 11) ]
print(list)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# List comprehensions with conditions
list = [i for i in range(1, 11) if i % 2 == 0]
print(list)  # [2, 4, 6, 8, 10]


