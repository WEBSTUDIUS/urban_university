class User:
    users = []

    def __init__(self, nickname, password, age=0):
        self.nickname = nickname
        self.password = password
        self.age = age

