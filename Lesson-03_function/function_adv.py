def pi():
    # result = 3.1415926
    # return result
    return 3.1415926


res = pi()

print("pi = ", res)

# ______________


def day_millis():
    return 24 * 60 * 60 * 1000


print(f"in one day: {day_millis()} millis")

# ______________


def greet(name):
    print("Hello, ", name)


greet("Jone!")

# ______________

# user__name = input("Enter you name: ")

# greet(user__name)

# ______________


def get_circumference(radius):
    return 2 * pi() * radius


res = get_circumference(60)
print("circumference =", res)
res = get_circumference(120)
print("circumference =", res)

# user_value = float(input("Enter you circumference value: ")) # !!! обязательно преобразовать в "число с плавающей точкой"
# radius = get_circumference(user_value)
# print("circumference =", radius)

# ______________

def years_to_millis(years):
  return years * 365 * day_millis()

years_millis = years_to_millis(7)
print("years in millis =", years_millis)

# ______________


def circle_area(radius):
  return pi() * radius ** 2


circle = circle_area(10)
print("circle area =", circle)

# ______________

