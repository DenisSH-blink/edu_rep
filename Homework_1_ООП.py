
from typing import Self


class BankAccount:
    
    __balance = 0

    def deposit(amount):
        Self.__balance += amount
    
    def withdraw(amount):
        Self.__balance -= amount
    
    def get_balance():
        return print(Self.__balance)

a = BankAccount()
a.deposit(1000)
a.withdraw(50)
a.get_balance()