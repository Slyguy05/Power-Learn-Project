def add():
    operators = ["+", "-", "*", "/"]
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("\nTry entering a number")
        return
    operator = input("Enter an operator (+, -, *, /): ")
    if operator not in operators:
        print("Operator must be one of (+, -, *, /)")
        return 
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2                
    return str(num1), operator, str(num2),  "=", str(result)

add()