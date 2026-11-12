# Topic: Using Try-Except to Handle Errors

# 1. Handling Division by Zero
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as err:
    print(err)

# 2. Handling Invalid User Input
try:
    number = int(input("Enter the number: "))
    print(number)
except ValueError:
    print("Invalid Input")