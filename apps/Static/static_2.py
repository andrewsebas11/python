class Employee:

    def func_message(self):
        print('Welcome to Programming')

    @staticmethod
    def func_msg():
        print("Welcome to Tutorial Gateway")


Employee.func_msg()

emp = Employee()
emp.func_message()


class Employee:

    def func_message(self):
        print('Welcome to The World')

    def func_addition(a, b):
        return a + b


Employee.func_addition = staticmethod(Employee.func_addition)
print('Total = ', Employee.func_addition(25, 50))

emp = Employee()
emp.func_message()


class Employee:

    def func_message(self):
        print('Welcome to Programming')

    @staticmethod
    def func_msg():
        print("Welcome to Tutorial Gateway")

    @staticmethod
    def split_string(message):
        return message.split(",")


Employee.func_msg()

countries = 'India, China, Japan, USA, UK, Australia, Canada'

print(Employee.split_string(countries))