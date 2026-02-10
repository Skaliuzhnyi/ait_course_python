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

age = 27
check = age >= 18 and age < 45  # оба условия верны и в результате check - true
print("check =", check)

age = 16
check = age >= 18 and age < 45 # одно из условий не верно и в результате check - false
print("check =", check)

age = 70
check = age >= 18 and age < 45 # одно из условий не верно и в результате check - false
print("check =", check)
