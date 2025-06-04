# Finally 

try:
    l= [1,2,3,4,5]
    i = input("Enter the index of the list to access: ")
    print(l[int(i)])
except:
    print("Index out of range! Please enter a valid index.")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")


# if we use print here ot will be executed but if we use it inside a function then it will not be
# executed but finally block will be executed inside a fuction

