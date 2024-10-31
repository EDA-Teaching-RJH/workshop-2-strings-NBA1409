import math
def safe_divide(a, b):
"""
Safely divide two numbers.
Args:
a (float): Numerator
b (float): Denominator
Returns:
float or str: Result of division or error message
"""
try:
return a / b
except ZeroDivisionError:
return "Cannot divide by zero"
def process_list(input_list):
"""
Calculate the sum of squares of integers in the list.
Args:
input_list (list): List of elements
Returns:
int: Sum of squares of integers
"""
total = 0
for item in input_list:
try:
num = int(item)
total += num ** 2
except (TypeError, ValueError):
continue
return total
def nested_operations(a, b):
"""
Perform nested operations: convert to int, divide, and square root.
Args:
a (any): First parameter
b (any): Second parameter
Returns:
float or str: Result of operations or error message
"""
try:
num1 = int(a)
num2 = int(b)
try:
division_result = num1 / num2
return math.sqrt(division_result)
except ZeroDivisionError:
return "Error: Division by zero"
except ValueError:
return "Error: Invalid input, please enter integers"
def process_input():
"""
Process user input to calculate square of a number.
Returns:
float or None: Square of the input number or None if error
"""
try:
user_input = input("Enter a number: ")
number = float(user_input)
except ValueError:
print("Error: Invalid input. Please enter a number.")
return None
else:
result = number ** 2
print(f"The square of {number} is {result}")
return result
finally:
print("Processing complete")
# Test the functions
main()
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(process_list([1, '2', 3, 'four', 5]))
print(nested_operations(16, 4))
print(nested_operations(10, 0))
print(nested_operations('a', 5))
process_input()
