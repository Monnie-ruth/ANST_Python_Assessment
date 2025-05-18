num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#choose an operation
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

# Perform the selected operation using conditionals
if operation == "add":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "divide":
    if num2 == 0:  # Prevent division by zero
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result is: {result}")
else:
    print("Invalid operation. Please choose add, subtract, multiply, or divide.")
