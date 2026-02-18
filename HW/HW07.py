result = 1

while True:
        number = int(input("Введите число: "))
        
        if number == 0:
            break
          
        if number % 2 == 0:
            result *= number  

print(f"Произведение всех четных чисел: {result}")