class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    def __len__(self):
        return len(self.marks)

    def __eq__(self, other):
        return self.marks == other.marks

student1 = Student("Harini", [80, 90, 85])
student2 = Student("Anu", [80, 90, 85])

print(student1)

print("Number of Subjects:", len(student1))

print("Same Marks:", student1 == student2)
