seta = {2, 3 ,4 ,2, 3, 4}  # Creating a set with duplicate elements

print(type(seta))  # Output: <class 'set'>

s = {}

print(type(s))  # Output: <class 'dict'>, because {} creates an empty dictionary by default

# Sets are unordered collections of unique elements
# They are mutable, meaning you can add or remove elements
# Sets are useful for membership testing, removing duplicates from a list, and performing mathematical set operations like union, intersection, and difference.
# Example of set operations

set1 = {1, 2, 3}    
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Output: {3}
print(set1.difference(set2))  # Output: {1, 2}
print(set2.difference(set1))  # Output: {4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# Sets can be created using curly braces or the set() constructor
set3 = {1, 2, 3}    
set4 = set([3, 4, 5])  # Using the set constructor

print(type(set4)) 

print(set3)  # Output: {1, 2, 3}
print(set4)  # Output: {3, 4, 5}

# # Sets can also be used to remove duplicates from a list
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print(unique_set)  # Output: {1, 2, 3, 4, 5}    

# Note: The output of the set will not maintain the order of elements as sets are unordered collections.