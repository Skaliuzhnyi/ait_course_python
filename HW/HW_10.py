def analyze_grades(grades):
    if not grades:
        print("\033[91mСписок оценок пуст. Пожалуйста, введите оценки.\033[0m")
        return

    print("Все оценки:", *grades)

    average = sum(grades) / len(grades)
    print("Средний балл:", average)

    count_above_avg = 0
    for grade in grades:
        if grade > average:
            count_above_avg += 1

    print("Количество оценок выше среднего:", count_above_avg)


grades_list = [5, 4, 3, 5, 2, 4, 5, 3]
analyze_grades(grades_list)
