def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b   # Corrected: division operator

def avg(a, b, c):
    return (a + b + c) / 3


print("Please select an operation:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Average\n")

select = int(input("Select an operation from 1,2,3,4,5: "))

# Taking inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if select == 1:
    print(a, "+", b, "=", add(a, b))

elif select == 2:
    print(a, "-", b, "=", sub(a, b))

elif select == 3:
    print(a, "*", b, "=", multi(a, b))

elif select == 4:
    print(a, "/", b, "=", div(a, b))

elif select == 5:
    c = int(input("Enter third number: "))
    print("Average of", a, b, c, "=", avg(a, b, c))

else:
    print("Invalid Selection!")

 

