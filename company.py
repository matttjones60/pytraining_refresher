from employee import Employee

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def pay_employees(self):
        for emp in self.employees:
            print(f"Paying {emp.name} their weekly salary of ${emp.calculate_salary():.2f}")

def main():
    my_company = Company("Tech Solutions")

    emp1 = Employee("Alice", "Developer", 80000)
    emp2 = Employee("Bob", "Designer", 70000)

    my_company.employees.append(emp1)
    my_company.employees.append(emp2)

    print(f"Company: {my_company.name}")
    for emp in my_company.employees:
        emp.display_info()
        print(f"Weekly Salary: ${emp.calculate_salary():.2f}")

main()