for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")



# but if i use break statement then else block will not execute
for x in range(5):
    if x == 3:
        break
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")

print ("Out of loop after break statement")