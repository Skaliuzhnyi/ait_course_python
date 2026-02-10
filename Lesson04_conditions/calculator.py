# operation typs: '+', '-', '*'. '/'

def calculator(a, b, operation):
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


calculator(2, 3, "-")
calculator(2, 3, "+")
calculator(2, 3, "*")
calculator(2, 3, "/")
calculator(2, 3, "$")
