# 1. Создать функцию, которая определяет сдал ли студент экзамен:
# Функция принимает три параметра: сдан ли первый зачет (bool),
# сдан ли второй зачет (bool), оценку по экзамену (int)
# функция возвращает True усли сданы оба зачета и оценка по эзамену больше 55
# 2. Попросить пользователя ввести с консоли информацию о сдачи зачетов
# и оценку по экзамену, данные сохранить в переменные
# 3. Вызвать функцию с введенными данными и результат сохранить в переменную
# 4. Распечатать значение переменной в консоли

""" 
def check_exam_result(exam_1: bool, exam_2: bool, grade: int):
    return exam_1 and exam_2 and grade > 55


input_exam_1 = input("\033[34mHave you passed exam 1? (yes/no) \033[0m").strip().lower()
input_exam_2 = input("\033[34mHave you passed exam 2? (yes/no) \033[0m").strip().lower()
input_grade = int(input("\033[34mEnter your rating from 0 to 100: \033[0m"))

exam_1 = input_exam_1 == "yes"
exam_2 = input_exam_2 == "yes"


result = check_exam_result(exam_1, exam_2, input_grade)
result_passed = f"\033[32mStudent passed!\033[0m"
result_failed = "\033[31mStudent failed!\033[0m \033[36mYou have not met all the requirements.\033[0m"

print(result_passed if result else result_failed)
"""


def check_exam_result(exam_1, exam_2, grade) -> bool:
    return exam_1 and exam_2 and grade > 55


# Ввод
exam_1 = input(
    "\033[34mHave you passed exam 1? (yes/no) \033[0m").strip().lower() == "yes"
exam_2 = input(
    "\033[34mHave you passed exam 2? (yes/no) \033[0m").strip().lower() == "yes"
grade = int(input("\033[34mEnter your rating from 0 to 100: \033[0m"))

# Проверка
result = check_exam_result(exam_1, exam_2, grade)

# Вывод
print(
    f"\033[32mStudent passed!\033[0m" if result
    else "\033[31mStudent failed!\033[0m \033[36mYou have not met all the requirements.\033[0m"
)
