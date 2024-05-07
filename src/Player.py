class Player:

    first_name_position = 1
    last_name_position = 2
    username_position = 0
    password_position = 3

    def __init__(self, raw_customer):
        self.first_name = raw_customer[self.first_name_position]
        self.last_name = raw_customer[self.last_name_position]
        self.username = raw_customer[self.username_position]
        self.password = raw_customer[self.password_position]

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_username(self):
        return self.username

    def compare_password(self, password):
        return password == self.password