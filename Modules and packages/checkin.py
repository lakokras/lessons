from register import *
from time import sleep
base_passw = {"Maria" : "uaa", "Ildar" : "zzz", "Dora" : "mnk", "Aizat" : "aaa"}


def login():
    
    passw = input("Введите пароль: ")
    
    password = base_passw.get(log)
    if password and password == passw:
        print("Доступ разрешён!")
    elif not password:
        register()
        base_passw[log] = passw
        print("Регистрация прошла успешно!")
    else:
        print("Доступ запрещён!")
        

def del_user():
    passw = input("Введите пароль: ")
    delet = input("Какой логин удалить? ")
    base_passw.pop(delet)
    sleep(0.7)
    print("подождите", end = " ")
    for i in range(3):
        sleep(0.3)
        print(".", end = " ")
    print("\nЛогин успешно удалён!")
    return delet