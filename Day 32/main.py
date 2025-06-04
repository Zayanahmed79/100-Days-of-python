set1 = {1,2,3}
set2 = {3,4,5}

print(set1.isdisjoint(set2))

# The isdisjoint() method returns True if two sets have a null intersection.
# In other words, it returns True if there are no common elements between the two sets.


set3 = {1,2,3,4,5}
set4 = {1,3,5}

print(set3.issuperset(set4))
print(set4.issubset(set3))


set3.add(6)
print(set3)
# The add() method adds an element to the set. If the element already exists, it will not be added again.

set3.remove(6)
print(set3)

# The remove() method removes an element from the set. If the element does not exist, it raises a KeyError.
# If you want to remove an element without raising an error if it does not exist, you can use the discard() method.
# Discard() does not raise an error if the element does not exist.
# remove() and discard() are similar, but remove() raises an error if the element does not exist, while discard() does not.

set5 = {1,2,3,4,5} 
set6= set5.pop()
print(set5) 
print(set6) # The pop() method removes and returns an arbitrary element from the set.
# The pop() method removes and returns an arbitrary element from the set.
# If the set is empty, it raises a KeyError.

# del set5
# print(set5) # This will raise a NameError because set5 has been deleted.
# The del statement deletes the set from memory.

# clear() method removes all elements from the set, but does not delete the set itself.
set5.clear()
print(set5)  # This will print an empty set: set()




set7 = {1,2,3,4,5}
set8 = {3,4,5,6,7}

