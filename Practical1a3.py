class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        
    def increment_salary(self, amount):
        self.salary += amount

# Creating object
e1 = Employee(1001, "Rahul", 40000)
e1.display()
e1.increment_salary(5000)

print("In After salary Increment :")
e1.display()