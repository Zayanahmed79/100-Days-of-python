# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")


matching = input("Enter matching words: ")

for i in matching.split():
    if i.isalpha():
        print(i)
    else:
        raise ValueError("Not a valid word")
    
