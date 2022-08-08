class Student():

    def __init__(self, ID, name, age, location, phone):
        self.ID = ID
        self.name = name
        self.age = age
        self.location = location
        self.phone = phone

    @staticmethod
    def printstudentdetails(ID, name, age, location, phone):
        print(f"Id = {ID}, Name = {name}, Age = {age}, Location = {location}, Contact = {phone} ")

Student.printstudentdetails(1, 'Andrew', 26, 'Chennai', 7904223237)