#Task 1: Calculate Factorial Using a Function 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result*=  i
    return result

number = int(input("Enter a number: "))

if number < 0:
    print("The number cannot be negative.")
else:
    fact = factorial(number)
    print(f"Factorial of", number, "is:", fact)

#Task 2: Using the Math Module for Calculations

import math

number = float(input("Enter a number: "))

sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)

print(f"Square root: {sqrt_result}")
print(f"Logarithm: {log_result}")
print(f"Sine: {sine_result}")