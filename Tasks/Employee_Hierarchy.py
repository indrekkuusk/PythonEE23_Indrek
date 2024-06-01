# Employee Hierarchy: Create an employee hierarchy (e.g., Employee, Manager, Executive) where each employee type has common
# attributes (e.g., name, ID, salary) and specific attributes/methods. Implement polymorphic methods such as calculating salary for each employee type.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


class Executive(Employee):
    def __init__(self, name, employee_id, salary, stock_options):
        super().__init__(name, employee_id, salary)
        self.stock_options = stock_options

    def calculate_salary(self):
        return super().calculate_salary() + self.stock_options


# Example usage:
employee1 = Employee("John Doe", 1001, 50000)
print("Employee 1 Salary:", employee1.calculate_salary())

manager = Manager("Alice Smith", 2001, 60000, 10000)
print("Manager Salary:", manager.calculate_salary())

executive = Executive("Bob Johnson", 3001, 80000, 20000)
print("Executive Salary:", executive.calculate_salary())

# This code defines a base class Employee with common attributes like name, employee ID, and salary, along with a method calculate_salary() which returns the salary.
# Then, two subclasses Manager and Executive are created with their own specific attributes (like bonus for managers and stock options for executives) and override
# the calculate_salary() method to include these additional benefits. This allows for polymorphic behavior when calculating salaries for different types of employees.