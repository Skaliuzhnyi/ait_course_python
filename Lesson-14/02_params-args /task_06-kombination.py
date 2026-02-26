def log(event, *args, **kwargs):
    print(event)
    print(args)
    print(kwargs)  
    print('-' * 20)
    
log('start process', 'python', 3.14, user='admin', level='info')