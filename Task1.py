# ANSI color codes
RED = "\033[31m"
RESET = "\033[0m"  # reset to default color
num1 = int(input(RED + "Enter the first number: " + RESET))
num2 = int(input(RED + "Enter the second number: " + RESET))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:

       division = num1 / num2   # will show decimal if needed

else:

     division = "Undefined"

# Display results in color
print(RED + "\n--- Results ---")
print(RED + f"Addition: {addition}" + RESET)
print(RED + f"Subtraction: {subtraction}" + RESET)
print(RED + f"Multiplication: {multiplication}" + RESET)
print(RED + f"Division: {division}" + RESET)