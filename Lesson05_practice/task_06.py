def check_number(number):
    positive = f"\033[93mNumber {number} is \033[35mpositive\033[0m"
    negative = f"\033[93mNumber {number} is \033[35mnegative\033[0m"

    if number > 0:
        return positive
    elif number < 0:
        return negative
    else:
        return f"\033[93mYou number is \033[35m'0' \033[93mand this is also a positive number!\033[0m"


user_number = int(input("\033[31mEnter you number: \033[0m"))

result = check_number(user_number)

print(result)
