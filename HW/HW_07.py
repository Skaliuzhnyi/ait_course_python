result = 1
has_even = False

while True:
    number = int(input("Введите число: "))

    if number == 0:
        break

    if number % 2 == 0:
        result *= number
        has_even = True

if has_even:
    print(f"Произведение всех четных чисел: {result}")
else:
    print("Четные числа не были введены.")
