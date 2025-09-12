class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary 

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")
    
    def calculate_salary(self):
        return self.salary/52