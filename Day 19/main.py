# Table of 5
print("Table of 5".center(60,"~"))
for i in range(1, 18):
    if i == 11 :
        print(f"Exiting at {i} as further is not allowed") 
        break
    print(f"5 x {i} = {5 * i}")


    # Break statement is used to exit the loop when a certain condition is met.# In this case, we are skipping the number 11 and breaking out of the loop.
# The loop will not print the multiplication for 11.

print("\n")
# Table of 2    

print("Table of 2".center(60,"~"))
# The loop will print the multiplication table of 2 from 1 to 17, skipping the number 11.
# Continue statement is used to skip the current iteration of the loop and move to the next iteration.for i in range(1, 18):
for a in range(1, 18):
    if a == 11:
        print(f"Skipping {i} as it is not allowed")
        continue    
    print(f"2 x {a} = {2 * a}")