# operation typs: '+', '-', '*'. '/'

""" 

def calculator(a, operation, b):
    text = f"{a} {operation} {b} ="

    if operation == "+":
        print(text, a + b)
    elif operation == "-":
        print(text, a - b)
    elif operation == "*":
        print(text, a * b)
    elif operation == "/":
        print(text, round(a / b, 2))
    else:
        print("Wrong operation typ")


calculator(2, "-", 3)
calculator(2, "+", 3)
calculator(2, "*", 3)
calculator(2, "/", 3)
calculator(2, "$", 3) 

"""


def calculator(a, operation, b):
    if operation == "+":
        result = a + b
        return result
    elif operation == "-":
        result = a - b
        return result
    elif operation == "*":
        result = a * b
        return result
    elif operation == "/" and b != 0:
        result = round(a / b, 2)
        return result
    else:
        return ("\033[96mWrong operation typ\033[0m")


calc_result = calculator(10, "+", 5)
print(calc_result)
calc_result = calculator(10, "/", 0)
print(calc_result)
calc_result = calculator(10, "/", 3)
print(calc_result)
calc_result = calculator(10, "-", 5)
print(calc_result)
calc_result = calculator(10, "*", 5)
print(calc_result)
calc_result = calculator(10, "%", 5)
print(calc_result)
