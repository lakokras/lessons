def login():
    BD = {}
    while True:
        login = input("Введите логин: ")
        parolka = input("Введите пароль: ")

        passw = BD.get(login)
        if passw == parolka:
            print("Вы успешно авторизовались")
        elif not passw:
            BD[login] = parolka
            print("Регистрация прошла успешно")
        else:
            print("Неверный пароль, доступ запрещен")
            break


login()