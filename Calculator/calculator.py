def calculator():

    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))

    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        result = a + b
        print("Result:", result)

    elif op == "-":
        result = a - b
        print("Result:", result)

    elif op == "*":
        result = a * b
        print("Result:", result)

    elif op == "/":
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            result = a / b
            print("Result:", result)

    else:
        print("Invalid operation")


calculator()
