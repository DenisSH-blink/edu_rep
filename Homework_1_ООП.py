class BankAccount:
    
    __balance = 0

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if ((self.__balance - amount) > 0):
            self.__balance -= amount
        else:
            return print('Недостаточно средств!')
    
    def get_balance(self):
        return print(self.__balance)

a = BankAccount()
a.deposit(1000)
a.withdraw(50)
a.get_balance()