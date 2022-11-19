def get_login():
    login = input("Введите логин: ")
    return login


def get_password():
    password = input("Введите пароль: ")
    return hash(password)
