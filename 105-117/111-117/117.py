from random import randint
FILENAME = "game.csv"

name = input("Введите свое имя: ")
questions = [
    "Какая у тебя фамилия? ", 
    "Как дела? ",
    "Что делаешь? ", 
    "Любимое хобби? ",
    "Любимый ЯП? ", 
    "Есть домашнее животное? ", 
    "Умеешь готовить? ", 
    "Да/нет? ",
    "Сколько стоит твой шмот? ",
    "Нападать или защищаться? "]

rand1 = randint(0, len(questions) - 1)
rand2 = randint(0, len(questions) - 1)
def check():
    if rand1 == rand2:
        rand2 = randint(0, len(questions) - 1)
        return check()
    return

answer1 = input(questions[rand1])
answer2 = input(questions[rand2])

fullAnswer1 = f"{name}, {questions[rand1]} {answer1}"
fullAnswer2 = f"{name}, {questions[rand2]} {answer2}"

file = open(FILENAME, "a")
file.write(f"{fullAnswer1}\n")
file.write(f"{fullAnswer2}\n")
file.close()

file = open(FILENAME, "r")
for row in file:
    print(row)

