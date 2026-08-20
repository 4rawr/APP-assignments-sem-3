class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.category = self.categorize_salary()

    def categorize_salary(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        return "Low Salary"

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary:,}, Category: {self.category}")


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all(self):
        for employee in self.employees:
            employee.display()
