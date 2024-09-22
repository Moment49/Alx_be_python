num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator_type = input("Choose the operation (+, -, *, /): ")

match operator_type:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        try:
            result = num1 / num2
            print(f"The result is {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        