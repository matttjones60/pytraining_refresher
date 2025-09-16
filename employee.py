class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_info(self):
        print(f"{self.name} - {self.role}")

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary()")


class SalaryEmployee(Employee):
    def __init__(self, name, role, annual_salary):
        super().__init__(name, role)
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary / 52


class HourlyEmployee(Employee):
    def __init__(self, name, role, hourly_rate, hours_worked):
        super().__init__(name, role)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, role, annual_salary, commission_rate, sales_made):
        super().__init__(name, role, annual_salary)
        self.commission_rate = commission_rate
        self.sales_made = sales_made

    def calculate_salary(self):
        regular_salary = super().calculate_salary()
        commission = self.commission_rate * self.sales_made
        return regular_salary + commission