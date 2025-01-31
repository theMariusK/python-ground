import datetime
from enum import Enum
from pydantic import BaseModel

class Type(Enum):
    groceries = 1
    clothing = 2
    health = 3
    utilities = 4
    others = 5

class Expense(BaseModel):
    title: str
    price: float
    exp_type: Type = Type.others
    time: datetime.datetime = datetime.datetime.now()

class User():
    def __init__(self, username : str, password : str):
        self.username = username
        self.__password = hash(password)
        self.expenses: list[Expense] = []

    def add_expense(self, expense : Expense) -> None:
        self.expenses.append(expense)

    def get_expenses(self) -> list:
        return self.expenses
