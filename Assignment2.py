#Task 1: Check if a Number is Even or Odd
number=int(input("Enter the number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
total_sum=0
for i in range(1,51):
    total_sum +=i
    print(f"The sum of numbers from 1 to 50 is: {total_sum}")