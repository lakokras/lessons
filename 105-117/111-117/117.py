from random import randint


fileName = "game.csv"

name = input("Введите свое имя: ")
questions = [
    "Какая у тебя фамилия? ", 
    "Как дела? ",
    "Что делаешь? ", 
    "Любимое хобби? ", 
    "Есть домашнее животное? ", 
    "Умеешь готовить? ", 
    "Да/нет? ",
    "Сколько стоит твой шмот? ",
    "Нападать или защищаться? "]


randint1 = randint(0, len(questions) - 1)
randint2 = randint(0, len(questions) - 1)

def check():
    if randint1 == randint2:
        randint22 = randint(0, len(questions) - 1)
        return check()
    return

answer1 = input(questions[randint1])
answer2 = input(questions[randint2])

fullAnswer1 = f"{name}, {questions[randint1]} {answer1}"
fullAnswer2 = f"{name}, {questions[randint2]} {answer2}"

file = open(fileName, "a")
file.write(f"{fullAnswer1}\n")
file.write(f"{fullAnswer2}\n")
file.close()

file = open(fileName, "r")

for row in file:
    print(row)
