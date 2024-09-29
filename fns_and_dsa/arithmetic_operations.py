def perform_operation(num1:float, num2:float, operation:str):
    """"A function to perform an arithmetic operation based on the type of operation selected"""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Not divisible by zero"
    else:
        return "Not a valid operation"