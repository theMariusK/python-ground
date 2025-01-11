import datetime
from enum import Enum

class Type(Enum):
    groceries = 1
    clothing = 2
    health = 3
    utilities = 4
    others = 5

class Expense:
    def __init__(self, title : str, price : float, exp_type : Type):
        self.title = title
        self.price = price
        self.exp_type = exp_type
        self.time = datetime.datetime.now()

class User:
    def __init__(self, username : str, password : str):
        self.username = username
        self.__password = hash(password)
        self.expenses: list[Expense] = []

    def add_expense(self, expense : Expense) -> None:
        self.expenses.append(expense)

    def get_expenses(self) -> list:
        return self.expenses
