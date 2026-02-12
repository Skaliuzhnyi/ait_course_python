def bank_work_time(day_of_week):
    if day_of_week == 6 or day_of_week == 7:
        return "Закрыто"
    if day_of_week == 1 or day_of_week == 3 or day_of_week == 5:
        return "8:30 - 13:30"
    if day_of_week == 2 or day_of_week == 4:
        return "8:30 - 13:30 и 16:00 - 18:00"
    # else:
    #     return "Неверный номер дня недели!"
    return "Неверный номер дня недели!"
    
day = int(input("Введите номер дня недели: "))
result = bank_work_time(day)
print(result)