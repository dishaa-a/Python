class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
       sum = 0
       for val in self.marks:
           sum += val
       return sum/len(self.marks)
    
s1 = Student("John", [85, 90, 95])
s2 = Student("Amit", [80, 90, 75])

print(s1.name, s1.avg())
print(s2.name, s2.avg())