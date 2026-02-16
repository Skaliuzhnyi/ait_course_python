# sum_digits(5712348)

def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10  # Получаем последнюю цифру числа
        total += digit  # Добавляем эту цифру к общей сумме
        # Удаляем последнюю цифру из числа (целочисленное деление на 10)
        n //= 10
    return total


number = int(input("\033[31mВведите число: \033[0m"))
sum_result = sum_digits(number)
print("\033[33mСумма цифр: \033[0m", sum_result)
