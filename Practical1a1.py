class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name) 
        print("Roll No:", self.roll_no) 
        print("Marks:", self.marks)

    def update_marks(self, new_marks): 
        self.marks = new_marks

# Creating object
st = Student("Alice", 101, 85) 
st.display() 

# Manipulating object
st.update_marks(92)

print("\nAfter updating marks:") 
st.display()