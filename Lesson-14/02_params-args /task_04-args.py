def sum_all(*args):
    result = 0

    for a in args:
        result += a
    return result


print(sum_all(1, 2, 3, 4, 5))
print(sum_all())
print(sum_all(10, -5, 2, 45, -23))

print('=== sum inputs data ===')

data = []
input_value = input("Enter number, or 's' to finish: ")
while input_value.lower() != 's':
    try:
        data.append(int(input_value))
    except ValueError:
        print("\033[31mError: You must enter valid simbols!\033[0m")
        
    input_value = input("Enter number, or 's' to finish: ")

print(f"You entered: {data}")
sum = sum_all(*data)
print(f"Sum of inputs: {sum}")