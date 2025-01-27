#Function to calculate factorial using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a positive integer: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
