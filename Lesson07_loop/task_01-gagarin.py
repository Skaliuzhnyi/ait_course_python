def gagarin():
    start_count = 10

    print("\033[35mПривет, я Юрий Гагарин!\033[0m")
    print("\033[35mЯ первый человек, полетевший в космос.\033[0m")

    while start_count >= 1:
        print(f"Обратный отсчет: {start_count}")
        start_count -= 1

    print("\033[31mПоехали!\033[0m")


gagarin()
