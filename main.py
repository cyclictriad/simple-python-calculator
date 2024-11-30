# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  if num2 == 0:
    print("Division by zero error!")
  else:
    result = num1 / num2
else:
  print("Invalid operation!")

# Print the result
if "operation" in locals():
  print(f"{num1} {operation} {num2} = {result}")