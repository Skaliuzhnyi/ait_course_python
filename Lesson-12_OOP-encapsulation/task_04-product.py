# Product: bar_code, name, price, unit (kg, l, item...)
# !! TODO Создать класс Product. Создать несколько продуктов и поместить их в список 
# Найти самый дорогой и самый дешевый продукт из списка
# Информацию о всех продуктах также вывестив консоль

class Product:
  def __init__(self, bar_code, name, price, unit):
      self.bar_code = bar_code
      self.name = name
      self.print = price
      self.unit = unit
      
  def __str__(self):
      return f'Name: {self.name}, Bar code: {self.bar_code}, Price: {self.price}, Unit: {self.unit}'
    
product_1 = [1233, 'tomato', 0.93, 'kg']
product_2 = [1234, 'milk', 1.33, 'l']
product_3 = [1235, 'eggs', 2.33, 'item']

products_list = [product_1, product_2, product_3]

