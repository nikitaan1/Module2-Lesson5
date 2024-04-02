def multiplication(a, b):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a * b

def division(a, b):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a / b

def addition(a, b):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))    
    return a + b

def subtraction(a, b):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a - b

#Task 2

print("Welcome:")
print("1. multiplication")
print("2. division")
print("3. addition")
print("3. subtraction")

choice = int(input("Select your desired operation "))

if choice == 1:
    multiplication()
elif choice == 2:
    division()
elif choice == 3:
    addition()
elif choice == 4:
    subtraction()
else:
    print("Invalid choice")
