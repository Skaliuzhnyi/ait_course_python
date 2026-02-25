#  Person: id, name, age
class Person:
    pass 
  
person_1 = Person()
person_1.id = 1
person_1.name = "Alice"
person_1.age = 30

print(f"Person 1:\n ID: {person_1.id},\n Name: {person_1.name},\n Age: {person_1.age}")

person_1.name = "Bob"
print(f"Updated Person 1 Name: {person_1.name}")
print(f"Person 1:\n ID: {person_1.id},\n Name: {person_1.name},\n Age: {person_1.age}")

person_2 = Person()
person_2.id = 2
person_2.name = "Charlie"
person_2.age = 25 

print(f"Person 2:\n ID: {person_2.id},\n Name: {person_2.name},\n Age: {person_2.age}")

person_3 = Person()
person_3.id = 3
person_3.name = "Diana"
person_3.age = 28

print(f"Person 3:\n ID: {person_3.id},\n Name: {person_3.name},\n Age: {person_3.age}")

print(person_1)
print(person_2)
print(person_3)

print("=== average age ===")
average_age = (person_1.age + person_2.age + person_3.age) / 3
print(average_age)

