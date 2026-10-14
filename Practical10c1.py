# Dictionary Lookup using Hashing

student = {
    101: "Rahul",
    102: "Priya",
    103: "Amit",
    104: "Neha"
}

roll_no = 102

if roll_no in student:
    print("Student Found")
    print("Roll No:", roll_no)
    print("Name:", student[roll_no])
else:
    print("Student Not Found")


