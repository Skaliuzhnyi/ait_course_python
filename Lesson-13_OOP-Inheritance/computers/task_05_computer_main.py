from task_02_computer import Computer
from task_03_laptop import Laptop
from task_04_smartphone import Smart_phone

computer_1 = Computer( 'Mac', 64, 2000, 'Apple')
laptop_1 = Laptop('M4', 64, '2Tb', 'Apple', '23 uhr', 1.433)
print("My computer - ", computer_1)
print("My laptop - ", laptop_1)

print('-' * 100)

laptop_2 = Laptop('M4', 128, '2Tb', 'Apple', '23 uhr', 2.433)
print("My laptop - ", laptop_2)

print('-' * 100)

smartphone = Smart_phone('ios', 128, 512, 'Iphone', '48 uhr', .333, 32444033)
print("My Smart Phone - ", smartphone)

print('-' * 100)

print(computer_1.is_windows11_compatible())