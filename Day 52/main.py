# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
# lambda x: x * 2



cube = lambda x  :( x**3 )

print(cube(2))  # Output: 35

# now put lambda function inside a function

def apply_function (x, y ):
    return 2 + x(y)

print(apply_function(cube,3)) 



