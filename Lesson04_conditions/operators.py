a = 10
b = -a
print(b)
b = -b
print(b)

# !! shorthand operators +=, -=, *=, /=

# a = a + 3
a += 3
# a = a - 4
a -= 4
print("a =", a)

# !! logical operators "and", "or", "not"

# and

age = 27
check = age >= 18 and age < 45  # оба условия верны и в результате 'check' - 'true'
print("check =", check)

age = 16
# одно из условий не верно и в результате 'check' - 'false'
check = age >= 18 and age < 45
print("check =", check)

age = 70
# одно из условий не верно и в результате 'check' - 'false'
check = age >= 18 and age < 45
print("check =", check)

# or

age = 21
check = age < 18 or age >= 45
print(f"check if {age} = {check}")

age = 18
check = age < 18 or age >= 45
print(f"check if {age} = {check}")

age = 70
check = age < 18 or age >= 45
print(f"check if {age} = {check}")

time = True
money = True
sponsor = False
traveling = True
traveling = time and (money or sponsor)
print(f"traveling is posible - {traveling}")
