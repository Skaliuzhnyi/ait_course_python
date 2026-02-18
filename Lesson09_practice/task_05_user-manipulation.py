numbers = []

user_input = input("Enter a number (or 'stop' to exit): ")
while user_input != 'stop':
    number = round(float(user_input))
    numbers.append(number)
    user_input = input("Enter a number (or 'stop' to exit): ")
    
print(f"Current numbers: {numbers}")
