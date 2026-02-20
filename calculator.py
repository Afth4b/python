logo = r"""
 _____________________
|  _________________  |
| | Pythonista   1.1 | |
| |_________________| |
|_____________________|
"""

# Basic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide by zero!")
        return None
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

# Main program
while True:
    num1 = float(input("Enter first number: "))

    print("\nChoose operation:")
    for op in operations:
        print(op)

    operator = input("Pick an operation: ")

    num2 = float(input("Enter second number: "))

    if operator in operations:
        result = operations[operator](num1, num2)

        if result is not None:
            print(f"\nResult: {num1} {operator} {num2} = {result}")
    else:
        print("Invalid operator!")

    again = input("\nDo you want to calculate again? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the calculator 😊")
        break