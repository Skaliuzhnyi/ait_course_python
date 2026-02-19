def check_height(height):
    meal = 300
    dish = meal
    if height > 190:
        dish = dish * 1.5  # dish *= 1.5
    return dish


height = 197
total_meal = round(check_height(height))

print(
    f"if the soldier's height is {height} centimeters - then the portion size is {total_meal} grams")

height = 177
total_meal = round(check_height(height))
print(
    f"if the soldier's height is {height} centimeters - then the portion size is {total_meal} grams")


# ________________________________________________________________________________________________________________

error = "You entered an incorrect time!"


def get_am_pm(hour):
    # return "AM" if hour >= 0 and hour < 12 else "PM"
    if (hour >= 0 and hour < 12):
        return "AM"
    elif (hour >= 12 and hour <= 23.59):
        return "PM"
    else:
        return error


hour = 14
am_pm = get_am_pm(hour)
print(f"If it's {hour} o'clock now, then it's {am_pm}")

hour = 8
am_pm = get_am_pm(hour)
print(f"If it's {hour} o'clock now, then it's {am_pm}")


def check_time(hour):
    am_pm = get_am_pm(hour)
    if am_pm != error:
        print(f"If it's {hour} o'clock now, then it's {am_pm}")
    else:
        print(am_pm)


check_time(12)
check_time(24)
check_time(8)
check_time(-3)


# ________________________________________________________________________________________________________________

# fan mode: 0 - Stop, 1 - Slow, 2 - Medium, 3 - Fast

def fan(mode):
    if mode == 0:
        print("Stop")
    elif mode == 1:
        print("Slow")
    elif mode == 2:
        print("Medium")
    elif mode == 3:
        print("Fasе")
    else:
        print("Invalid mode! Try again please.")


fan(0)
fan(1)
fan(2)
fan(3)
fan(4)
fan(-10)
