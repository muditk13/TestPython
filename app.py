def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is undefined."

print("Welcome to the Basic Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in {'1', '2', '3', '4'}:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} × {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} ÷ {num2} = {result}")
    else:
        print("Invalid choice! Please select a valid operation.")
