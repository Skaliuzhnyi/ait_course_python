# print_colors.py

# ANSI коды для цветов
# from print_colors import red, green, blue, bold
RESET = "\033[0m"
BOLD = "\033[1m"

# Обычные цвета


def black(text): return f"\033[30m{text}{RESET}"
def red(text): return f"\033[31m{text}{RESET}"
def green(text): return f"\033[32m{text}{RESET}"
def yellow(text): return f"\033[33m{text}{RESET}"
def blue(text): return f"\033[34m{text}{RESET}"
def magenta(text): return f"\033[35m{text}{RESET}"
def cyan(text): return f"\033[36m{text}{RESET}"
def white(text): return f"\033[37m{text}{RESET}"

# Яркие цвета


def bright_black(text): return f"\033[90m{text}{RESET}"
def bright_red(text): return f"\033[91m{text}{RESET}"
def bright_green(text): return f"\033[92m{text}{RESET}"
def bright_yellow(text): return f"\033[93m{text}{RESET}"
def bright_blue(text): return f"\033[94m{text}{RESET}"
def bright_magenta(text): return f"\033[95m{text}{RESET}"
def bright_cyan(text): return f"\033[96m{text}{RESET}"
def bright_white(text): return f"\033[97m{text}{RESET}"

# Дополнительно: жирный текст


def bold(text): return f"{BOLD}{text}{RESET}"


# Пример использования при запуске файла напрямую
if __name__ == "__main__":
    print(red("Ошибка!"))
    print(green("Успех!"))
    print(blue("Информация"))
    print(bold("Жирный текст"))


earnings = 1500
print(f"Your salary: {green(earnings)}$ - {red('Not paid yet')}")
print(bold("This is important"))
