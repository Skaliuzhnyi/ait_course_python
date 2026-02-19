def check_number(number):
    try:
        number_checked = int(number)

        even = f"\033[93mNumber {number_checked} is \033[35meven \033[93mnumber\033[0m"
        odd = f"\033[93mNumber {number_checked} is \033[35modd \033[93mnumber\033[0m"

        if number_checked % 2 == 0:
            return even
        else:
            return odd

    except ValueError:
        print("\033[31mError: You must enter an integer!\033[0m")


user_number = input("\033[94mEnter you number: \033[0m")
result = check_number(user_number)

print(result)





