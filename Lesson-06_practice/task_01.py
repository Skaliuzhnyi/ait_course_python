def is_traveling(time, money, sponsor):
    traveling = time and (money or sponsor)
    return traveling


time = bool(input("Есть у Вас время на путешествие? "))
money = bool(input("Есть у Вас деньги на путешествие? "))
sponsor = bool(input("Есть у Вас спонсор для путешествия? "))

traveling = is_traveling(time, money, sponsor)
print('traveling =', traveling)
