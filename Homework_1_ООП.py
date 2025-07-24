from abc import ABC, abstractmethod
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


class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary
    
    def get_info(self):
        return print("Имя:" + self.__name + ' Должность:' + self.__position + ' Зарплата:' + str(self.__salary))


class Developer(Employee):
    __programming_langue = 'Python'
    def set_prog_langue(self, programming_langue):
        self.__programming_langue = programming_langue
    
    def get_info(self):
        return print("Имя:" + self.__name + ' Должность:' + self.__position + ' Зарплата:' + str(self.__salary) + ' Язык программирования:' + self.__programming_langue)


class Manager(Employee):
    __employees = []
    def set_employees(*args):
        pass
    
    def get_info(self):
        return print("Имя:" + self.__name + ' Должность:' + self.__position + ' Зарплата:' + str(self.__salary) + '\nСотрудники:' + self.__employees)
    

class Shape:
    def area():
        pass
    
    def perimetr():
        return 0
    
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    def area(self):
        return self.__width * self.__height
    
    def perimetr(self):
        return (self.__width*2) + (self.__height*2)

    
class Round(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return 2 * 3.14 * self.__radius**2
    
    def perimetr(self):
        return 3.14 * self.__radius


class Transport(ABC):
    def start_engine():
        pass
    
    def stop_engine():
        pass
    
    def move():
        pass


class Car(Transport):
    
    def start_engine():
        print('Start')
    
    def stop_engine():
        print('Stop')
    
    def move():
        print('Move -->')


class Boat(Transport):
    
    def start_engine():
        print('Boat start...')
        
    def stop_engine():
        print('Boat stop...')
    
    def move():
        print('Boat move... -->')
 
        
class Flyable:
    def fly():
        print('Fly!')


class Swimmable:
    def swim():
        print('Swim!')


class Duck(Flyable, Swimmable):
    def male_sound():
        print('Quack!')
        

class Animal(ABC):
    def speak():
        pass
    
    def move():
        pass
    

class Dog(Animal):
    def speak():
        print('Woof!')
        
    def move():
        print('Running...')


class Bird(Animal, Flyable):
    def speak():
        print('Tweet!')
    
    def move(self):
        self.fly()
    
class Fish(Animal, Swimmable):
    def speak():
        print('Silence...')
        
    def move(self):
        self.swim()


class Logger:
    instance = None
    __list_logs = []
    def __new__(cls, *args, **kwargs):
        if instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def log(cls, massage:str):
        cls.__list_logs.append(massage)
    
    def get_logs(cls):
        for i in cls.__list_logs:
            print(i)
    

class Report:
    def __init__(title, content):
        self.title = title
        self.content = content


class Generate_PDF(Report):
    def generate(self):
        print('Generating...')
    

class Save_file(Report):
    def save_to_file(self,filename: str):
        print('Saving...')


class PaymentType(ABC):
    def pay():
        pass
    
class PayPal(PaymentType):
    def pay():
        print('PayPal paying...')

class Stripe(PaymentType):
    def pay():
        print('Stripe paying...')
        
class PaymentProccesor:
    def pay(pay_type:PaymentType):
        return pay_type.pay()
    

class Bird(ABC):
    def make_sound():
        pass


class Sparrow(Bird):
    def make_sound():
        return print("I`am Sparrow")


class Penguin(Bird):
    def make_sound():
        return print("I`am Penguin")

class Animal(ABC):
    @abstractmethod
    def make_action(self):
        pass

class Fly(Animal):
    def make_action(self):
        print('Fly!')

class Run(Animal):
    def make_action(self):
        print('Run!')
        

class Swim(Animal):
    def make_action(self):
        print('Swim!')
        
class Lion:
    def __init__(self, animal_action:Animal):
        self.animal_action = animal_action
    
    def make_action(self):
        self.animal_action.make_action(self)


class Temperature:
    def __init__(temperature_cel:float):
        self.__temperature_cel = temperature_cel

    @classmethod
    def convert_to_fahrenheit(cls):
        cls.__fahrenheit = cls.__temperature_cel * 33.8
        return cls.__fahrenheit
    
    @property
    def kelvin(cls):
        return cls.__temperature_cel * 274.15
    
    @staticmethod
    def check_ice(cls):
        if cls.__temperature_cel <= 0:
            return print('Wather is freeze')
        return print('Water is warm')