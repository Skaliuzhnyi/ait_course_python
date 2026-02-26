def greeting(name, msg):
    print(f'{msg}, {name}!')
    
greeting('Bob', 'Hello')
greeting(msg='Hi', name='Bob')
greeting('Bob', msg='Hi')
# greeting(name='Alisa', 'Yo') !! TypeError - Нельзя сначала указывать именнованые аргкументы, а потом позиционные

