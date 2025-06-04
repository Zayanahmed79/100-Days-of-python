tup = (1,3,5,7,9)

print(type(tup), tup)

print(tup[0])  # Accessing the first element
print(tup[1])  # Accessing the second element   
print(tup[2])  # Accessing the third element


if 342 in tup:
    print("342 is in the tuple")
else:
    print("342 is not in the tuple")

# Attempting to change an element in the tuple will raise an error
# tup[0] = 10  # Uncommenting this line will raise a TypeError
# Tuples are immutable, so we cannot change their elements

# However, we can create a new tuple with the desired changes
new_tup = (10,"Zayan" )+ tup[1:]  # Create a new tuple with the first element changed
print("New tuple:", new_tup)