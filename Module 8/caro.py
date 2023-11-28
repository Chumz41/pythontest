class Car:
    def __init__(self, name, email, pay):
        self.name = name
        self.email = email
        self.pay = pay

    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_pay(self):
        return self.pay
    def set_name(self, new_name):
        self.name = new_name
    def set_email(self, new_email):
        self.mail = new_email 