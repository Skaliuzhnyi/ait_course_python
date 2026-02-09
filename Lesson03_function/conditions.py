def barmen(age):
    vol = 42 if age >= 18 else 1.5
    print(f"Max vol for age {age} is {vol}")


barmen(20)

# ______________


def get_max(a, b):
    return a if a > b else b


result = get_max(4, 6)
print("Max =", result)

# ______________


def check_role_admin(role):
    message = "Allowed" if role == "Administrator" else "Forbidden (404)"
    return message


print(check_role_admin("Administrator"))
print(check_role_admin("User"))

# ______________


def get_min(a, b):
    return a if a < b else b


result = get_min(4, 6)
print("Min =", result)
