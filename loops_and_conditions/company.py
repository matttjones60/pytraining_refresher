from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self, name):
        self.employees = []
    
    def display_employees(self):
        print(f"Current employees:")
        for emp in self.employees:
            print(f"- {emp.name}")
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def pay_employees(self):
        for emp in self.employees:
            print(f"Paying {emp.name} their weekly salary of ${emp.calculate_salary():.2f}")

def main():
    my_company = Company("Tech Solutions")

    emp1 = SalaryEmployee("Alice", "Developer", 80000)
    my_company.employees.append(emp1)
    emp2 = HourlyEmployee("Bob", "Designer", 25, 50)
    my_company.employees.append(emp2)
    emp3 = CommissionEmployee("Charlie", "Salesperson", 50000, 0.10, 20000)
    my_company.employees.append(emp3)

    my_company.pay_employees()
    my_company.display_employees()

main()