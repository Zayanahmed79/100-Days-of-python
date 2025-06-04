def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))


# f(0) = 0 
# f(1) = 1
# f(2) = f(1) = f(0)
# f(3) = f(2) + f(1) = 1 + 0 = 2
# f(4) = f(3) + f(2) = 1 + 1 = 3
# f(5) = f(4) + f(3) = 2 + 1 = 5
# f(6) = f(5) + f(4) = 3 + 2 = 8
# f(7) = f(6) + f(5) = 5 + 3 = 13


def fibonacci(n):
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
            return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))





