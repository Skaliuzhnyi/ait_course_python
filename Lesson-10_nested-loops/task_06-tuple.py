seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
print(seasons)

print('-' * 100)

print(seasons[0])  # Spring

print('-' * 100)

# seasons[0] = 'Весна'  # TypeError: 'tuple' object does not support item assignment

for season in seasons:
    print(season)

print('-' * 100)

seasons_list = list(seasons)
print(seasons_list)

print('-' * 100)

print('Autumn' in seasons)  # True
print('Весна' in seasons)  # False

print('-' * 100)

middles = seasons[1:3]
print(middles)

print('_' * 100)
