# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Base class 2
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Position: {self.position}"

# Derived class using multiple inheritance
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        # Initialize both base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def get_manager_info(self):
        # Combine information from both base classes
        person_info = Person.get_info(self)
        employee_info = Employee.get_employee_info(self)
        return f"{person_info}, {employee_info}, Department: {self.department}"

# Example usage
if __name__ == "__main__":
    # Create an instance of Manager
    manager = Manager("Alice", 35, "E123", "Manager", "Sales")
    
    # Display manager information
    print(manager.get_manager_info())
