# Functions

def CalculateMean(a , n):
    mean = (a*n)/(a+n) 
    print(f"The mean of {a} and {n} is {mean}")

def ChoseGreater(a , n):
    if a > n :
        print(f"{a} is greater than {n}")
    elif a == n:
        print(f"{a} is equal to {n}")
    else:
        print(f"{n} is greater than {a}")

CalculateMean(10, 20)
ChoseGreater(10, 20) 
ChoseGreater(20, 10)