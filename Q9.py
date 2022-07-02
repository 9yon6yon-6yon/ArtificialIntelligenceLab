class Employee:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

employees = []
N = int(input())
for i in range(N):
    name = input()
    height = int(input())
    age = int(input())
    emp = Employee(name, height, age)
    employees.append(emp)


employees.sort(key=lambda x: (x.height, x.age), reverse=True)
for i in employees:
    print(emp.name, emp.height, emp.age)
