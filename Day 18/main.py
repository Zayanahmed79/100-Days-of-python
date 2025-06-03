# Day 18 - While Loop Example
# i = 0
# while(i < 5):
#     print(i)
#     i += 1

# print("Loop ended")

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
  
  # this loop will continue until a non-positive number is entered and will print the entered negative number for the forst time