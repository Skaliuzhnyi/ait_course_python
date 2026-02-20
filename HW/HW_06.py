def is_office_open(hours, is_weekend, is_holiday):
    in_morning = 8 <= hours <= 12
    in_evening = 14 <= hours <= 18

    return (not is_weekend) and (not is_holiday) and (in_morning or in_evening)

hours = 10
is_weekend = False
is_holiday = False

result = is_office_open(hours, is_weekend, is_holiday)
print(f"Офис открыт? – {result}")
