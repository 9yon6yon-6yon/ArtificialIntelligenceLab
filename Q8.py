class Student(object):

    def __init__(self, id, name, cgpa=0.0):
        self.id = id
        self.name = name
        self.cgpa = cgpa

    def update_cgpa(self,cgpa):
        self.cgpa = cgpa
    def __str__(self) -> str:
        return "%d %s %.2f" % (self.id,self.name,self.cgpa)
students = {}
N = int(input("Enter how many : "))
for i in range(N):
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    student = Student(id,name)
    students[id] = student

M = int(input("Enter M: "))
for i in range (M):
    id = int(input("Enter id: "))
    cgpa = float(input("Enter CGPA: "))
    student.update_cgpa(cgpa)

for id in students:
    print(id,'--',students[id])    