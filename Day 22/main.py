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

