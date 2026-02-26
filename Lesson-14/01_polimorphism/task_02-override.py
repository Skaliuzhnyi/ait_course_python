from computers.task_02_computer import Computer
from computers.task_03_laptop import Laptop
from computers.task_04_smartphone import Smart_phone

computer_1 = Computer( 'Mac', 32, 2000, 'Apple')
laptop_1 = Laptop('M4', 64, '2Tb', 'Apple', '23 uhr', 1.433)
laptop_2 = Laptop('M4', 128, '2Tb', 'Apple', '23 uhr', 2.433)
smartphone = Smart_phone('ios', 128, 512, 'Iphone', '48 uhr', .333, 32444033)

def install_windows11(computer):
    if(computer.is_windows11_compatible()):
        print(f"Install Windows 11 on {computer}")
    else:
        print(f"Windows 11 is not compatible with {computer}")


install_windows11(computer_1)
install_windows11(laptop_1)
install_windows11(laptop_2)
install_windows11(smartphone)