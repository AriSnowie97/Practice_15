class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Місто: {self.city}")


person1 = Person("Іван", 30, "Київ")
person1.display_info()

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_full_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}, Колір: {self.color}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Колір автомобіля змінено на {self.color}.")

car1 = Car("Toyota", "Camry", 2022, "Сірий")
car1.display_full_info()
car1.change_color("Чорний")
car1.display_full_info()

class BankAccount:
    def __init__(self, owner_name, account_number):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Рахунок поповнено на {amount}. Новий баланс: {self.balance}")
        else:
            print("Сума поповнення повинна бути більшою за нуль.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"З рахунку знято {amount}. Новий баланс: {self.balance}")
            else:
                raise ValueError("Недостатньо коштів на рахунку.")
        else:
            print("Сума зняття повинна бути більшою за нуль.")

    def check_balance(self):
        print(f"Баланс рахунку {self.account_number}: {self.balance}")

account1 = BankAccount("Петро", "UA1234567890")
account1.deposit(1000)
account1.check_balance()

try:
    account1.withdraw(500)
    account1.check_balance()
    account1.withdraw(1500)
except ValueError as e:
    print(f"Помилка: {e}")

account1.check_balance()