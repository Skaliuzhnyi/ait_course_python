fruits = ["apple", "banana", "cherry", "date",
          "elderberry", "fig", "grape", "honeydew"]
print(fruits)
print(len(fruits))  # Выводим количество элементов в списке

fruits[3] = "dragonfruit"  # !! Изменяем элемент с индексом 3
print(fruits)
print(len(fruits))  # Выводим количество элементов в списке

fruits.append("kiwi")  # !! Добавляем новый элемент в конец списка
print(fruits)
print(len(fruits))  # Выводим количество элементов в списке

fruits.append("watermalon")  # !! Добавляем новый элемент в конец списка
print(fruits)
print(len(fruits))  # Выводим количество элементов в списке

# !! Вставляем новый элемент на позицию с индексом 2
fruits.insert(2, "blueberry")
print(fruits)
print(len(fruits))  # Выводим количество элементов в списке

print(fruits[0])  # Выводим первый элемент списка
print("Последний элемент в списке fruits - ", fruits[-1])
print("Третий с конца элемент в списке fruits - ", fruits[-3])
print(fruits[2:5])  # Выводим элементы с индексами от 2 до 4 (5 не включительно)
print(fruits[:4])  # Выводим первые 4 элемента списка
print(fruits[4:])  # Выводим элементы с индексами от 4 до конца списка
print(fruits[::2])  # Выводим каждый второй элемент списка
print(fruits[1::2])  # Выводим каждый второй элемент списка, начиная с индекса 1
print(fruits[::-1])  # Выводим список в обратном порядкеp
print(fruits[-3:])  # Выводим последние 3 элемента списка

del fruits[1]  # !! Удаляем элемент с индексом 1
print(fruits)
print(len(fruits))  # Выводим количество элементов в списке

remouved_fruit = fruits.pop()  # !! Удаляем и сохраняем последний элемент списка
print(fruits)
print(f"Удаленный элемент: {remouved_fruit}")

remouved_fruit = fruits.pop(5)  # !! Удаляем и сохраняем элемент с индексом 5
print(fruits)
print(f"Удаленный элемент: {remouved_fruit}")

# Метод remove удаляет первый найденный элемент по значению. Если такого элемента нет, то возникает ошибка.
fruits.remove("blueberry")  # !! Удаляем элемент по значению
print(fruits)

# sort
print("Исходный список: ", fruits)
sorted_list = sorted(fruits)  # !! Сортируем список и сохраняем результат в новый список  
print("Отсортированный список: ", sorted_list)

fruits.sort()  # !! Сортируем список на месте
print("Отсортированный список: ", fruits)

fruits.sort(reverse=True)  # !! Сортируем список в обратном порядке на месте
print("Отсортированный в обратном порядке список: ", fruits)

fruits.reverse()  # !! Разворачиваем порядок элементов в списке на месте
print("Развернутый список: ", fruits)
