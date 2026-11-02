import math

print("=== SCIENTIFIC CALCULATOR ===")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")

choice = input("Choose an operation: ")

if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)

elif choice == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)

elif choice == "3":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)

elif choice == "4":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero!")

elif choice == "5":
    a = float(input("Enter a number: "))

    if a >= 0:
        print("Result:", math.sqrt(a))
    else:
        print("Error: Invalid number!")

else:
    print("Invalid choice!")
