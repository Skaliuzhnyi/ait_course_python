def barmen(age):
    vol = 42 if age >= 18 else 1.5
    print(f"Max vol for age {age} is {vol}")


barmen(20)

# ______________


def get_max(a, b):
    return a if a > b else b


result = get_max(4, 6)
print("Max =", result)
