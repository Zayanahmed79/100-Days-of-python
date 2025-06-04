 
def average(*numbers):
    if not numbers:
        print("No numbers provided")
        return
    if not all(isinstance(i, (int, float)) for i in numbers):
        print("All inputs must be numbers")
        return
    if len(numbers) == 0:
        print("No numbers provided")
        return
    if len(numbers) == 1:
        print(numbers[0])
        return
    sum = 0
    for i in numbers:
        sum = sum + i
    print( sum /len(numbers) )

average("zz")  # All inputs must be numbers
average(1, 2, 3)  # 2.0 
average(1, 2, 3, 4, 5)  # 3.0
average(1)  # 1
average()  # No numbers provided
average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 5.5



