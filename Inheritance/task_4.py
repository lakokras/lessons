class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print(f"Я - {self.login}. Могу просматривать содержимое.")


class Moderator(User):
    def __init__(self, group_id):
        super().__init__("Модератор", "мяукаю")
        self.group_id = group_id

    def view(self):
        print(f"Я - {self.login}. Могу просматривать содержимое.")

    def redact(self):
         print(f"Я - {self.login}. Могу просматривать содержимое.")


user_1 = User("Морда", "бебебе")
user_2 = Moderator("Модератор")
user_1.view()
user_2.view()
user_2.redact()
