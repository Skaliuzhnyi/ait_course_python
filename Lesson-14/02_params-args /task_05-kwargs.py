def shoe_settings(**kwargs):
    for key, val in kwargs.items():
        print(f'{key}: {val}')

    print('-' * 20)


shoe_settings(theme='dark', lang='en', size='medium')
shoe_settings(width=640, height=480, ppi=3.2)
