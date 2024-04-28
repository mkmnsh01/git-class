def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 
# Test the factorial function
number = 7
print("The factorial of", number, "is", factorial(number))
