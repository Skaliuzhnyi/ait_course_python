user_input = input("Enter a number, or 'stop' to quit: ")
accum = 0
count = 0
while user_input != 'stop':
    number = float(user_input)
    accum += number # accum = accum + number
    count += 1 # count = count + 1
    user_input = input("Enter a number, or 'stop' to quit: ")

avg = accum / count
print(f"Average = {avg}")