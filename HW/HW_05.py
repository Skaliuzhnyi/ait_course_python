working_day = False
vacation = False


def what_is_day_today(is_working_day, is_vacation):
    return is_working_day and not is_vacation


result = what_is_day_today(working_day, vacation)
print(result)

print(f"Нужно ли сегодня идти на работу? – {result}")
